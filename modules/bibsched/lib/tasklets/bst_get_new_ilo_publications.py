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

def bst_get_new_ilo_publications(number_results_to_display=5):
    """
    Bibtasklet responsible of the generation of the list
    containing the most recent ILO publications.
    @param number_results_to_display: number of results to display
    to users in main page.
    """

    task_update_progress("Start calculating new ILO publications")

    ILO_publications_recids = perform_request_search(p="992__a:'ILO publication'")
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
