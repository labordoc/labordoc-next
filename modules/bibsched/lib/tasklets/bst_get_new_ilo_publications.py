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

import os
from invenio.search_engine import perform_request_search
from invenio.config import CFG_TMPDIR
from invenio.bibtask import task_update_progress
from invenio.search_engine import get_creation_date
from invenio.dbquery import run_sql
import datetime
import dateutil.relativedelta


def bst_get_new_ilo_publications(number_results_to_display=5):
    """
    Bibtasklet responsible of the generation of the list
    containing the most recent ILO publications and to update
    automatically the query to get the most recent ILO publications.
    @param number_results_to_display: number of results to display
    to users in main page.
    """

    task_update_progress("Start updating query for collection Latest publications by ILO")
    # get current month and get the 2 previous ones
    now = datetime.datetime.now()
    month_1 = (now + dateutil.relativedelta.relativedelta(months=-1)).month
    month_2 = (now + dateutil.relativedelta.relativedelta(months=-2)).month
    # update also tab collection where id=113
    dbquery = """(946__d:2013-%s-* or 946__d:2013-%s-* or 946__d:2013-%s-*) and (997__a:2012 or 997__a:2013) and (992__a:"ILO publication") not callno:GB.* not callno:NYP""" % (now.month, month_1, month_2)
    query = """update collection set dbquery='%s' where id=113;""" % dbquery
    run_sql(query)
    task_update_progress("Finished updating query for collection Latest publications by ILO")

    task_update_progress("Start calculating new ILO publications")
    ILO_publications_recids = perform_request_search(p=dbquery)
    dict_creation_date_per_recid = {}
    for recid in ILO_publications_recids:
        dict_creation_date_per_recid.update({recid:get_creation_date(recid,
                                                                     fmt="%Y-%m-%d %H:%i:%S")})

    sorted_dict_creation_date_per_recid = sorted(dict_creation_date_per_recid.items(),
                                                 key=lambda x:x[1])
    new_ilo_publications = sorted_dict_creation_date_per_recid[-int(number_results_to_display):]
    new_ilo_publications.reverse()
    new_ilo_publications_recids = [t[0] for t in new_ilo_publications]
    new_ilo_publications_file = open(CFG_TMPDIR + "/new_ILO_publications", "w")
    new_ilo_publications_file.write(repr(new_ilo_publications_recids))
    new_ilo_publications_file.close()
    task_update_progress("Finished calculating new ILO publications")
