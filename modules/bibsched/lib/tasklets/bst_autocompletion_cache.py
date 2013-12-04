# -*- coding: utf-8 -*-
##
## This file is part of Invenio.
## Copyright (C) 2013 CERN.
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

from invenio.bibtask import task_update_progress
from invenio.websearch_external_collections_utils import get_collection_name_by_id
from invenio.search_engine import get_field_tags, \
                                  get_most_popular_field_values, \
                                  get_collection_reclist
from invenio.websearch_model import AutocompletionCache, Collection
from invenio.sqlalchemyutils import db
from invenio.dbquery import run_sql


def bst_autocompletion_cache(collection_list=None):
    """
    Bibtasklet responsible of the generation of the subjects and authors list for the
    autocompletion suggestions.
    @param collection_list: list of collection ids to cache.
                            If None, all the collections will be calculated.

    """

    task_update_progress("Started updating autocomplete cache")

    tag_dicc = {'en': '9051_a', 'fr': '9061_a', 'es': '9071_a'}

    if collection_list == None:
        res = run_sql("SELECT id FROM collection")
        collection_list = [i[0] for i in res]

    i = 0
    task_update_progress("Done %s of %s" % (i, len(collection_list)))
    for collection in collection_list:
        i += 1
        recids = list(get_collection_reclist(get_collection_name_by_id(collection)))
        authors = get_most_popular_field_values(recids, get_field_tags('exactauthor'))[0:200]
        authors = [a[0] for a in authors]

        subjects = {}
        for ln in ['en', 'fr', 'es']:
            subject_tag = tag_dicc[ln]
            subjects[ln] = [s[0] for s in get_most_popular_field_values(recids, subject_tag)]

        ins = AutocompletionCache(id_collection=collection, authors=authors, subjects=subjects)
        db.session.merge(ins)
        db.session.flush()
        task_update_progress("Done %s of %s" % (i, len(collection_list)))


    db.session.close_all()
    task_update_progress("Finished updating autocomplete cache")
