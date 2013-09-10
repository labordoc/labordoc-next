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
"""BibFormat element - Prints titles for the CIP data
"""
__revision__ = "$Id$"

import cgi
import re

def format_element(bfo, separator="", highlight='no'):
    """
    Prints the titles of a record.

    @param separator: separator between the different titles
    @param highlight: highlights the words corresponding to search query if set to 'yes'
    """
    titles = []

    title = bfo.field('245%%a')
    title_remainder = bfo.field('245%%b')

    if len(title) > 0:
        title = re.sub('/$', '', title)
        title = re.sub(' $', '', title)
        if title_remainder:
            title_remainder = re.sub('/$', '', title_remainder)
            title_remainder = re.sub(' $', '', title_remainder)
            title_remainder = re.sub(' : ', ': ', title_remainder)
            title += ' ' + title_remainder
            title = title.replace('::', ':')
        titles.append( title )

        tstring = separator.join(titles)
        #tstring = tstring + "."
        #tstring = tstring.replace("&#x2019;", "'")
        if not '&#' in tstring: 
            tstring = cgi.escape(tstring)
        return tstring


def escape_values(bfo):
    """
    Called by BibFormat in order to check if output of this element
    should be escaped.
    """
    return 0






