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
"""BibFormat element - Prints titles with link to detailed record
"""
__revision__ = "$Id$"

def format_element(bfo, separator=" ", highlight='no'):
    """
    Prints the titles of a record. Makes a link to detailed record.

    @param separator: separator between the different titles
    @param highlight: highlights the words corresponding to search query if set to 'yes'
    """
    import cgi
    import re
    from invenio.urlutils import create_html_link
    from invenio.messages import gettext_set_language
    from invenio.config import CFG_SITE_URL

    _ = gettext_set_language(bfo.lang)    # load the right message language


    recid = bfo.control_field('001') 
    ln = ''

    titles = []

    title = bfo.field('24510a')
    title_remainder = bfo.field('24510b')
    edition_statement = bfo.field('25010a')
    title_tome = bfo.field('24510n')
    title_part = bfo.field('24510p')

    if len(title) == 0:
        title = bfo.field('245__a')
        title_remainder = bfo.field('245__b')
        edition_statement = bfo.field('250__a')
        title_tome = bfo.field('245__n')
        title_part = bfo.field('245__p')
    
    if len(title) == 0:
        title = bfo.field('24511a')
        title_remainder = bfo.field('24511b')
        edition_statement = bfo.field('25011a')
        title_tome = bfo.field('24511n')
        title_part = bfo.field('24511p')

    if len(title) == 0:
        title = bfo.field('24512a')
        title_remainder = bfo.field('24512b')
        edition_statement = bfo.field('25012a')
        title_tome = bfo.field('24512n')
        title_part = bfo.field('24512p')

    if len(title) == 0:
        title = bfo.field('24513a')
        title_remainder = bfo.field('24513b')
        edition_statement = bfo.field('25013a')
        title_tome = bfo.field('24513n')
        title_part = bfo.field('24513p')

    if len(title) == 0:
        title = bfo.field('24514a')
        title_remainder = bfo.field('24514b')
        edition_statement = bfo.field('25014a')
        title_tome = bfo.field('24514n')
        title_part = bfo.field('24514p')

    if len(title) == 0:
        title = bfo.field('24515a')
        title_remainder = bfo.field('24515b')
        edition_statement = bfo.field('25015a')
        title_tome = bfo.field('24515n')
        title_part = bfo.field('24515p')

    if len(title) == 0:
        title = bfo.field('24516a')
        title_remainder = bfo.field('24516b')
        edition_statement = bfo.field('25016a')
        title_tome = bfo.field('24516n')
        title_part = bfo.field('24516p')

    if len(title) == 0:
        title = bfo.field('24517a')
        title_remainder = bfo.field('24517b')
        edition_statement = bfo.field('25017a')
        title_tome = bfo.field('24517n')
        title_part = bfo.field('24517p')

    if len(title) == 0:
        title = bfo.field('24518a')
        title_remainder = bfo.field('24518b')
        edition_statement = bfo.field('25018a')
        title_tome = bfo.field('24518n')
        title_part = bfo.field('24518p')

    if len(title) == 0:
        title = bfo.field('24519a')
        title_remainder = bfo.field('24519b')
        edition_statement = bfo.field('25019a')
        title_tome = bfo.field('24519n')
        title_part = bfo.field('24519p')

    if len(title) == 0:
        title = bfo.field('24500a')
        title_remainder = bfo.field('24500b')
        edition_statement = bfo.field('25000a')
        title_tome = bfo.field('24500n')
        title_part = bfo.field('24500p')

    if len(title) == 0:
        title = bfo.field('24501a')
        title_remainder = bfo.field('24501b')
        edition_statement = bfo.field('25001a')
        title_tome = bfo.field('24501n')
        title_part = bfo.field('24501p')

    if len(title) == 0:
        title = bfo.field('24502a')
        title_remainder = bfo.field('24502b')
        edition_statement = bfo.field('25002a')
        title_tome = bfo.field('24502n')
        title_part = bfo.field('24502p')

    if len(title) == 0:
        title = bfo.field('24503a')
        title_remainder = bfo.field('24503b')
        edition_statement = bfo.field('25003a')
        title_tome = bfo.field('24503n')
        title_part = bfo.field('24503p')

    if len(title) == 0:
        title = bfo.field('24504a')
        title_remainder = bfo.field('24504b')
        edition_statement = bfo.field('25004a')
        title_tome = bfo.field('24504n')
        title_part = bfo.field('24504p')

    if len(title) == 0:
        title = bfo.field('24505a')
        title_remainder = bfo.field('24505b')
        edition_statement = bfo.field('25005a')
        title_tome = bfo.field('24505n')
        title_part = bfo.field('24505p')

    if len(title) == 0:
        title = bfo.field('24506a')
        title_remainder = bfo.field('24506b')
        edition_statement = bfo.field('25006a')
        title_tome = bfo.field('24506n')
        title_part = bfo.field('24506p')

    if len(title) == 0:
        title = bfo.field('24507a')
        title_remainder = bfo.field('24507b')
        edition_statement = bfo.field('25007a')
        title_tome = bfo.field('24507n')
        title_part = bfo.field('24507p')

    if len(title) == 0:
        title = bfo.field('24508a')
        title_remainder = bfo.field('24508b')
        edition_statement = bfo.field('25008a')
        title_tome = bfo.field('24508n')
        title_part = bfo.field('24508p')

    if len(title) == 0:
        title = bfo.field('24509a')
        title_remainder = bfo.field('24509b')
        edition_statement = bfo.field('25009a')
        title_tome = bfo.field('24509n')
        title_part = bfo.field('24509p')

    if len(title) > 0:
        if title_remainder:
            title += ': ' + title_remainder
            title = title.replace('::', ':')
        if len(title_tome) > 0:
            title += ", " + title_tome
        if len(title_part) > 0:
            title += ": " + title_part
            title = title.replace(':', ':')
        title = re.sub('/$', '', title)
        title = re.sub(':$', '', title)
        titles.append( title )

    title = bfo.field('0248_a')
    if len(title) > 0:
        titles.append( title )

    title = bfo.field('246__a')
    if len(title) > 0:
        titles.append( title )

    title = bfo.field('246__b')
    if len(title) > 0:
        titles.append( title )

    title = bfo.field('246_1a')
    if len(title) > 0:
        titles.append( title )

    if len(titles) > 0:
        #Display 'Conference' title only if other titles were not found
        title = bfo.field('111__a')
        if len(title) > 0:
            titles.append( title )

    #titles = [cgi.escape(x) for x in titles]

    if highlight == 'yes':
        from invenio import bibformat_utils
        titles = [bibformat_utils.highlight(x, bfo.search_pattern) for x in titles]

    lang = '?ln='+ bfo.lang
    target = '<a href="%s/record/%s%s">'  % (CFG_SITE_URL, recid, lang)


    # make a detailed record link
    if len(edition_statement) > 0:
        return target + separator.join(titles) + "; " + edition_statement + "</a>"
    else:
        return target + separator.join(titles) + "</a>"

def escape_values(bfo):
    """
    Called by BibFormat in order to check if output of this element
    should be escaped.
    """
    return 0






