# -*- coding: utf-8 -*-
##
## This file is part of Invenio.
## Copyright (C) 2011, 2012, 2013 CERN.
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

from invenio.title_descending import title_descending
from invenio.author_descending import author_descending
from invenio.publication_date_descending import publication_date_descending
from invenio.publication_date_ascending import publication_date_ascending

def bst_update_ilo_kb_files():
    """
    """
    title_descending("/opt/invenio/etc/bibrank/ILO_title_descending.kb")

    author_descending("/opt/invenio/etc/bibrank/ILO_author_descending.kb")

    publication_date_descending("/opt/invenio/etc/bibrank/ILO_year_title.kb")

    publication_date_ascending("/opt/invenio/etc/bibrank/ILO_year_title_ascending.kb")
