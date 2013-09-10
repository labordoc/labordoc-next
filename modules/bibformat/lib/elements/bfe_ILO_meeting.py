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
"""BibFormat element - Prints meeting info
"""
__revision__ = "$Id$"

import cgi
import re

def format_element(bfo, separator=" ", highlight='no'):
    """
    Prints the meeting information.

    @param separator: separator between the different titles
    @param highlight: highlights the words corresponding to search query if set to 'yes'
    """
    meeting = []

    name = bfo.field('1112_a')
    session_no = bfo.field('1112_n')
    date = bfo.field('1112_d')
    place = bfo.field('1112_c')
    rnum1 = bfo.field('4901_a')
    rnum2 = bfo.field('4901_v')
    rnum3 = bfo.field('4901_x')

    if len(name) == 0:
        name = bfo.field('7112_a')
    if len(session_no) == 0:
        session_no = bfo.field('7112_n')
    if len(date) == 0:
        date = bfo.field('7112_d')
    if len(place) == 0:
        place = bfo.field('7112_c')

    if len(name) > 0:
        meeting.append(name)
    if len(session_no) > 0:
        meeting.append(session_no)
    if len(date) > 0:
        meeting.append(date)
    if len(place) > 0:
        meeting.append(place)
    if len(rnum1) > 0:
        meeting.append(rnum1)
    if len(rnum2) > 0:
        meeting.append(rnum2)
    if len(rnum3) > 0:
        meeting.append(rnum3)

    meeting = [cgi.escape(x) for x in meeting]

    if highlight == 'yes':
        from invenio import bibformat_utils
        meeting = [bibformat_utils.highlight(x, bfo.search_pattern) for x in meeting]

    return separator.join(meeting)

def escape_values(bfo):
    """
    Called by BibFormat in order to check if output of this element
    should be escaped.
    """
    return 0






