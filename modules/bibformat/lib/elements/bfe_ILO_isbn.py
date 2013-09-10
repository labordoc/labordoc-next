# -*- coding: utf-8 -*-
##
## This file is part of Invenio.
## Copyright (C) 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010 CERN.
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
"""BibFormat element - Print ISBN
"""

__revision__ = "$Id$"

from invenio.websubmit_functions.Create_Modify_Interface import Create_Modify_Interface_getfieldval_fromDBrec
from invenio.bibupload import find_record_from_sysno
#value =  Create_Modify_Interface_getfieldval_fromDBrec('8564_u',440333)
#value = find_record_from_sysno('LABORDOC-447053')

def format_element(bfo, separator=", "):
    """
    Returns the ISBN of the record.
    """
    isbn_numbers = bfo.fields("020__a")
    isbn_numbers_no_pdf = []

    for isbn in isbn_numbers:
        if isbn.find('pdf') >= 1:
            pass
        else:
            isbn_numbers_no_pdf.append(isbn)

    return separator.join(isbn_numbers_no_pdf)

def escape_values(bfo):
    """
    Called by BibFormat in order to check if output of this element
    should be escaped.
    """
    return 0



