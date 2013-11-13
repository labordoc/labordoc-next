# -*- coding: utf-8 -*-

## This file is part of Invenio.
## Copyright (C) 2012, 2013 CERN.
##
## Invenio is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 2 of the
## License, or (at your option) any later version.
##
## Invenio is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with Invenio; if not, write to the Free Software Foundation, Inc.,
## 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

import os
from operator import itemgetter
from itertools import groupby
from werkzeug.utils import cached_property
from flask import g, url_for, request, abort, current_app

from invenio.websearch_cache import search_results_cache, \
                                    get_search_results_cache_key_from_qid, \
                                    get_pattern_from_cache, \
                                    get_collection_name_from_cache
from invenio.intbitset import intbitset
from invenio.config import CFG_WEBSEARCH_SEARCH_CACHE_TIMEOUT, CFG_PYLIBDIR
from invenio.importutils import autodiscover_modules
from invenio.webuser_flask import current_user
from invenio.websearch_model import Collection
from invenio.search_engine import search_pattern, \
                                  get_field_tags, \
                                  get_records_that_can_be_displayed, \
                                  get_most_popular_field_values, \
                                  get_fieldvalues

from invenio.config import CFG_SITE_LANG
from invenio.messages import gettext_set_language, wash_language
from invenio.websearch_external_collections_utils import get_collection_id


def get_current_user_records_that_can_be_displayed(qid):
    """
    Returns records that current user can display.

    @param qid: query identifier

    @return: records in intbitset
    """
    @search_results_cache.memoize(timeout=CFG_WEBSEARCH_SEARCH_CACHE_TIMEOUT)
    def get_records_for_user(qid, uid):
        key = get_search_results_cache_key_from_qid(qid)
        data = search_results_cache.get(key)
        if data is None:
            return intbitset([])
        cc = search_results_cache.get(key + '::cc')
        return get_records_that_can_be_displayed(current_user,
                                                 intbitset().fastload(data), cc)
    # Simplifies API
    return get_records_for_user(qid, current_user.get_id())


def faceted_results_filter(recids, filter_data, facets):
    """
    Returns records that match selected filter data.

    @param recids: found records
    @param filter_date: selected facet filters
    @param facet_config: facet configuration

    @return: filtered records
    """

    ## Group filter data by operator and then by facet key.
    sortkeytype = itemgetter(0)
    sortfacet = itemgetter(1)
    data = sorted(filter_data, key=sortkeytype)
    out = {}
    for t, vs in groupby(data, key=sortkeytype):
        out[t] = {}
        for v, k in groupby(sorted(vs, key=sortfacet), key=sortfacet):
            out[t][v] = map(lambda i: i[2], k)

    filter_data = out

    ## Intersect and diff records with selected facets.
    output = recids

    if '+' in filter_data:
        values = filter_data['+']
        for key, facet in facets.iteritems():
            if key in values:
                output.intersection_update(facet.get_facet_recids(values[key]))

    if '-' in filter_data:
        values = filter_data['-']
        for key, facet in facets.iteritems():
            if key in values:
                output.difference_update(facet.get_facet_recids(values[key]))

    return output


def _facet_plugin_checker(plugin_code):
    """
    Handy function to bridge importutils with (Invenio) facets.
    """
    if 'facet' in dir(plugin_code):
        candidate = getattr(plugin_code, 'facet')
        if isinstance(candidate, FacetBuilder):
            return candidate
    raise ValueError('%s is not a valid facet plugin' % plugin_code.__name__)


class FacetLoader(object):

    @cached_property
    def plugins(self):
        """Loaded facet plugins."""
        return map(_facet_plugin_checker,
                   autodiscover_modules(['invenio.websearch_facets'],
                                        'facet_.+\.py'))

    @cached_property
    def elements(self):
        """Dict with `FacetBuilder` instances accesible by facet name."""
        return dict((f.name, f) for f in self.plugins)

    def __getitem__(self, key):
        return self.elements[key]

    @cached_property
    def sorted_list(self):
        """List of sorted facets by their order property."""
        return sorted(self.elements.values(), key=lambda x: x.order)

    def config(self, *args, **kwargs):
        """Returns facet config for all loaded plugins."""
        pattern = get_pattern_from_cache(kwargs.get('qid'))
        collection_name = get_collection_name_from_cache(kwargs.get('qid'))
        collection_id = get_collection_id(collection_name)
        collection_id_set = intbitset()
        collection_id_set.add(collection_id)
        descendants = Collection.query.get(collection_id).descendants_ids

        if pattern == "" and descendants.difference(collection_id_set):
           facets_list = filter(lambda x: x.order == 1, self.sorted_list)
        else:
            facets_list = self.sorted_list
        return map(lambda x: x.get_conf(*args, **kwargs), facets_list)


class FacetBuilder(object):
    """Implementation of a general facet builder using function
    `get_most_popular_field_values`."""

    def __init__(self, name, order=0):
        self.name = name
        self.order = order

    def get_title(self, **kwargs):
        return g._('Any ' + self.name.capitalize())

    def get_url(self, qid=None):
        return url_for('.facet', name=self.name, qid=qid)

    def get_conf(self, **kwargs):
        return dict(title=self.get_title(**kwargs),
                    url=self.get_url(kwargs.get('qid')),
                    facet=self.name)

    def get_recids_intbitset(self, qid):
        try:
            return get_current_user_records_that_can_be_displayed(qid)
        except:
            return intbitset([])

    def get_recids(self, qid):
        return list(self.get_recids_intbitset(qid))

    def get_facets_for_query(self, qid, limit=20, parent=None):
        return get_most_popular_field_values(self.get_recids(qid),
                                             get_field_tags(self.name)
                                             )[0:limit]

    #@blueprint.invenio_memoize(timeout=CFG_WEBSEARCH_SEARCH_CACHE_TIMEOUT / 2)
    def get_value_recids(self, value):
        if isinstance(value, unicode):
            value = value.encode('utf8')
        p = '"' + str(value) + '"'
        return search_pattern(p=p, f=self.name)

    #@blueprint.invenio_memoize(timeout=CFG_WEBSEARCH_SEARCH_CACHE_TIMEOUT / 4)
    def get_facet_recids(self, values):
        return reduce(lambda x, y: x.union(y),
                      [self.get_value_recids(v) for v in values],
                      intbitset())


class CollectionFacetBuilder(FacetBuilder):
    """Custom implementation of collection facet builder."""

    def get_title(self, **kwargs):
        """Returns title for collection facet."""
        collection = kwargs.get('collection')
        if collection is not None and collection.id > 1:
            return collection.name_ln
        return super(CollectionFacetBuilder, self).get_title(**kwargs)

    def get_facets_for_query(self, qid, limit=20, parent=None):
        recIDsHitSet = self.get_recids_intbitset(qid)
        parent = request.args.get('parent', None)
        if parent is not None:
            collection = Collection.query.filter(Collection.name == parent).\
                                          first_or_404()
        else:
            cc = search_results_cache.get(
                    get_search_results_cache_key_from_qid(qid) + '::cc')
            if cc is not None:
                collection = Collection.query.filter(Collection.name == cc).\
                                          first_or_404()
            else:
                collection = Collection.query.get(1)
        facet = []
        for c in collection.collection_children_r:
            num_records = len(c.reclist.intersection(recIDsHitSet))
            if num_records:
                facet.append((c.name, num_records, c.name_ln))
        return sorted(facet, key=lambda x: x[1], reverse=True)[0:limit]


class FulltextFacetBuilder(FacetBuilder):
    """Custom implementation of fulltext facet builder."""

    def get_title(self, **kwargs):
        return g._('Attached fulltext')

    def get_facets_for_query(self, qid, limit=20, parent=None):
        facet = get_most_popular_field_values(self.get_recids(qid),
                                              get_field_tags(self.name)
                                              )[0:limit]
        return filter(lambda x: x[0] == "Yes", facet)


class LanguageFacetBuilder(FacetBuilder):
    """Custom implementation of language facet builder."""

    def get_facets_for_query(self, qid, limit=20, parent=None):
        from invenio.search_engine_config import CFG_LANGUAGE_DICT as language_dict
        facet = get_most_popular_field_values(self.get_recids(qid),
                                              get_field_tags(self.name)
                                              )[0:limit]
        nicer_facet = []
        for i in facet:
            if i[0] in language_dict.keys():
                nicer_facet.append((i[0], i[1], language_dict[i[0]]))
            elif i[0] not in ('N/A',):
                nicer_facet.append(i[0], i[1], i[0])
        return nicer_facet


class YearFacetBuilder(FacetBuilder):
    """Custom implementation of year facet builder."""

    def get_facets_for_query(self, qid, limit=20, parent=None):
        facet = get_most_popular_field_values(self.get_recids(qid),
                                             get_field_tags(self.name)
                                             )[0:limit]
        return sorted(facet, key=lambda x: x[0], reverse=True)


#    def get_facets_for_query(self, qid, limit=20, parent=None):
#        all_facets = get_most_popular_field_values(self.get_recids(qid),
#                                       get_field_tags(self.name))
#        fulltext_facets = {'Full text': 0, 'Booklet': 0}
#        for i in all_facets:
#            if i[0].startswith("Full"):
#                fulltext_facets["Full text"] = fulltext_facets["Full text"] + i[1]
#            elif i[0].startswith("Booklet"):
#                fulltext_facets["Booklet"] = fulltext_facets["Booklet"] + i[1]
#            elif i[0].startswith("http"):
#                pass
#            else:
#                fulltext_facets[i[0]] = i[1]
#        if fulltext_facets["Full text"] == 0:
#            fulltext_facets.pop("Full text")
#        if fulltext_facets["Booklet"] == 0:
#            fulltext_facets.pop("Booklet")
#
#        res = fulltext_facets.items()
#        res.sort(key=lambda tup: tup[1], reverse=True)
#        return res
