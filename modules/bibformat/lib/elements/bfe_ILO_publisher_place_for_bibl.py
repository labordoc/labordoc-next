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
"""BibFormat element - Prints publisher name
"""
__revision__ = "$Id$"

import re
import cgi

def format_element(bfo):
    """
    Prints publisher info for bibl format
    @see: place.py, date.py, reprints.py, imprint.py, pagination.py
    """  

    publisher = ""

    publisher_a = bfo.field('260__a')
    publisher_b = bfo.field('260__b')
    publisher_c = bfo.field('260__c')

    if len(publisher_a) > 0:
        publisher = publisher_a + " " + publisher_b + " " + publisher_c
    
    else:
        in_t = bfo.field('7730_t')
        in_d = bfo.field('7730_d')
        in_g = bfo.field('7730_g')
        publisher = " <i>in</i> " + in_t
        if len(in_d) > 0: 
            publisher += " (" + in_d + ")"
        if len(in_g) > 0:
            publisher += " " + in_g

    if publisher != "sine nomine":
        return publisher

def escape_values(bfo):
    """
    Called by BibFormat in order to check if output of this element
    should be escaped.
    """
    return 0


