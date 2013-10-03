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
"""BibFormat element - Prints keywords
"""
__revision__ = "$Id$"

import cgi
from urllib import quote
from invenio.config import CFG_SITE_URL


def format_element(bfo, prefix_en="", prefix_es="",
                   prefix_fr="", link='yes'):
    """
    Display keywords of the record according to interface language. Default is English.
    @param link: links the keywords if 'yes' (HTML links)
    """

    if bfo.lang == 'fr':
        keywords = bfo.fields('9061_a')
        if len(keywords) == 0:
            keywords = bfo.fields('90617a')
    elif bfo.lang == 'es':
         keywords = bfo.fields('9071_a')
         if len(keywords) == 0:
             keywords = bfo.fields('90717a')
    else:
        keywords = bfo.fields('9051_a')
        if len(keywords) == 0:
            keywords = bfo.fields('90517a')

    if len(keywords) > 0:
        if bfo.lang == 'es':
            prefix = prefix_es
        elif bfo.lang == 'fr':
            prefix = prefix_fr
        else:
            prefix = prefix_en

        separator = "&nbsp;&nbsp"

        if link == 'yes':
            keywords = ['<span><a href="' + CFG_SITE_URL + '/search?f=subject&amp;p='+ \
                        quote('"' + keyword + '"') + \
                        '&amp;ln='+ bfo.lang+ \
                        '"><span class="label label">' + cgi.escape(keyword) + '</span></a></span>'
                        for keyword in keywords]
        else:
            keywords = [cgi.escape(keyword)
                        for keyword in keywords]

        final_keywords = prefix + separator.join(keywords)

        return final_keywords


def escape_values(bfo):
    """
    Called by BibFormat in order to check if output of this element
    should be escaped.
    """
    return 0
