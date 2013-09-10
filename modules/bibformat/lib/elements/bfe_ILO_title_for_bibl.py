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
    Prints the titles of a record. Makes a link to detailed record. Formats according to bibl.

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

    title_a = bfo.field('24510a')
    title_h = bfo.field('24510h')
    title_b = bfo.field('24510b')
    title_n = bfo.field('24510n')
    title_p = bfo.field('24510p')
    title_c = bfo.field('24510c')
    

    if len(title_a) == 0:
        title_a = bfo.field('245__a')
        title_h = bfo.field('245__h')
        title_b = bfo.field('245__b')
        title_n = bfo.field('245__n')
        title_p = bfo.field('245__p')
        title_c = bfo.field('245__c')

    if len(title_a) == 0:
        title_a = bfo.field('24511a')
        title_h = bfo.field('24511h')
        title_b = bfo.field('24511b')
        title_n = bfo.field('24511n')
        title_p = bfo.field('24511p')
        title_c = bfo.field('24511c')

    if len(title_a) == 0:
        title_a = bfo.field('24512a')
        title_h = bfo.field('24512h')
        title_b = bfo.field('24512b')
        title_n = bfo.field('24512n')
        title_p = bfo.field('24512p')
        title_c = bfo.field('24512c')

    if len(title_a) == 0:
        title_a = bfo.field('24513a')
        title_h = bfo.field('24513h')
        title_b = bfo.field('24513b')
        title_n = bfo.field('24513n')
        title_p = bfo.field('24513p')
        title_c = bfo.field('24513c')

    if len(title_a) == 0:
        title_a = bfo.field('24514a')
        title_h = bfo.field('24514h')
        title_b = bfo.field('24514b')
        title_n = bfo.field('24514n')
        title_p = bfo.field('24514p')
        title_c = bfo.field('24514c')

    if len(title_a) == 0:
        title_a = bfo.field('24515a')
        title_h = bfo.field('24515h')
        title_b = bfo.field('24515b')
        title_n = bfo.field('24515n')
        title_p = bfo.field('24515p')
        title_c = bfo.field('24515c')

    if len(title_a) == 0:
        title_a = bfo.field('24516a')
        title_h = bfo.field('24516h')
        title_b = bfo.field('24516b')
        title_n = bfo.field('24516n')
        title_p = bfo.field('24516p')
        title_c = bfo.field('24516c')

    if len(title_a) == 0:
        title_a = bfo.field('24517a')
        title_h = bfo.field('24517h')
        title_b = bfo.field('24517b')
        title_n = bfo.field('24517n')
        title_p = bfo.field('24517p')
        title_c = bfo.field('24517c')

    if len(title_a) == 0:
        title_a = bfo.field('24518a')
        title_h = bfo.field('24518h')
        title_b = bfo.field('24518b')
        title_n = bfo.field('24518n')
        title_p = bfo.field('24518p')
        title_c = bfo.field('24518c')

    if len(title_a) == 0:
        title_a = bfo.field('24519a')
        title_h = bfo.field('24519h')
        title_b = bfo.field('24519b')
        title_n = bfo.field('24519n')
        title_p = bfo.field('24519p')
        title_c = bfo.field('24519c')

    if len(title_a) == 0:
        title_a = bfo.field('24500a')
        title_h = bfo.field('24500h')
        title_b = bfo.field('24500b')
        title_n = bfo.field('24500n')
        title_p = bfo.field('24500p')
        title_c = bfo.field('24500c')

    if len(title_a) == 0:
        title_a = bfo.field('24501a')
        title_h = bfo.field('24501h')
        title_b = bfo.field('24501b')
        title_n = bfo.field('24501n')
        title_p = bfo.field('24501p')
        title_c = bfo.field('24501c')

    if len(title_a) == 0:
        title_a = bfo.field('24502a')
        title_h = bfo.field('24502h')
        title_b = bfo.field('24502b')
        title_n = bfo.field('24502n')
        title_p = bfo.field('24502p')
        title_c = bfo.field('24502c')

    if len(title_a) == 0:
        title_a = bfo.field('24503a')
        title_h = bfo.field('24503h')
        title_b = bfo.field('24503b')
        title_n = bfo.field('24503n')
        title_p = bfo.field('24503p')
        title_c = bfo.field('24503c')

    if len(title_a) == 0:
        title_a = bfo.field('24504a')
        title_h = bfo.field('24504h')
        title_b = bfo.field('24504b')
        title_n = bfo.field('24504n')
        title_p = bfo.field('24504p')
        title_c = bfo.field('24504c')

    if len(title_a) == 0:
        title_a = bfo.field('24505a')
        title_h = bfo.field('24505h')
        title_b = bfo.field('24505b')
        title_n = bfo.field('24505n')
        title_p = bfo.field('24505p')
        title_c = bfo.field('24505c')

    if len(title_a) == 0:
        title_a = bfo.field('24506a')
        title_h = bfo.field('24506h')
        title_b = bfo.field('24506b')
        title_n = bfo.field('24506n')
        title_p = bfo.field('24506p')
        title_c = bfo.field('24506c')

    if len(title_a) == 0:
        title_a = bfo.field('24507a')
        title_h = bfo.field('24507h')
        title_b = bfo.field('24507b')
        title_n = bfo.field('24507n')
        title_p = bfo.field('24507p')
        title_c = bfo.field('24507c')

    if len(title_a) == 0:
        title_a = bfo.field('24508a')
        title_h = bfo.field('24508h')
        title_b = bfo.field('24508b')
        title_n = bfo.field('24508n')
        title_p = bfo.field('24508p')
        title_c = bfo.field('24508c')

    if len(title_a) == 0:
        title_a = bfo.field('24509a')
        title_h = bfo.field('24509h')
        title_b = bfo.field('24509b')
        title_n = bfo.field('24509n')
        title_p = bfo.field('24509p')
        title_c = bfo.field('24509c')

#######################

    if len(title_a) > 0:
        title_a += ' ' + title_h
        title_a += ' ' + title_b
        title_a += ' ' + title_n
        title_a += ' ' + title_p
        titles.append( title_a )

    if len(titles) > 0:
        #Display 'Conference' title only if other titles were not found
        title = bfo.field('111__a')
        if len(title) > 0:
            titles.append( title_a )

    #titles = [cgi.escape(x) for x in titles]

    if highlight == 'yes':
        from invenio import bibformat_utils
        titles = [bibformat_utils.highlight(x, bfo.search_pattern) for x in titles]

    lang = '?ln='+ bfo.lang
    target = '<a href="%s/record/%s%s">'  % (CFG_SITE_URL, recid, lang)


    # make a detailed record link
    if len(title_c) > 0:
        return target + "<b>" + separator.join(titles) + "</b>" + "</a> " + title_c
    else:
        return target + "<b>" + separator.join(titles) + "</b>" + "</a> "

def escape_values(bfo):
    """
    Called by BibFormat in order to check if output of this element
    should be escaped.
    """
    return 0






