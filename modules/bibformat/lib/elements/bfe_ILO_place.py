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
"""BibFormat element - Prints imprint publication place
"""
__revision__ = "$Id$"

import re

def format_element(bfo):
    """
    Prints the imprint publication place as HTML
    Print only if there is no publisher field
    @see: date.py, publisher.py, reprints.py, imprint.py, pagination.py
    """

    publisher = bfo.field('260__b')
    place = bfo.field('260__a')

    if len(place) == 0:
        place = bfo.field('7730_d')

    place = re.sub(':$', '', place)
    place = re.sub(',$', '', place)

    if len(publisher) != 0:
        place = ''

    if place != "sine loco":
        return place



