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
"""BibFormat element - Prints record as XML
"""
__revision__ = "$Id$"

import urllib2
import re

def format_element(bfo, prefix, suffix):
    """
    Prints the javascript for redirecting to Voyager holdings.

    @param prefix and suffix
    """
    out = ''
    request_url = 'joo'
    voyager_sysno = bfo.field("970__a")
    voyager_sysno = re.sub('^LABORDOC-', '', voyager_sysno)
    #voyager_url = """http://golf.ilo.org/cgi-bin/Pwebrecon.cgi?bbid=%s""" % (voyager_sysno)
    voyager_url = """http://ringo.ilo.org:7008/vwebv/patronRequests?&sk=en_ILO&bibId=%s""" % (voyager_sysno)
    request = urllib2.Request(voyager_url)
    #request.add_header('UserAgent', 'Ruel.ME Sample Scraper')
    response = urllib2.urlopen(request)
    data=response.read().split("</A>")
    tag="<A HREF=\""
    endtag="\">"
    for item in data:
         if "<A HREF" in item and "Requests" in item:
             try:
                 ind = item.index(tag)
                 item=item[ind+len(tag):]
                 end=item.index(endtag)
             except: pass
             else:
                 request_url = item[:end]

    out = '<a href="http://golf.ilo.org' + request_url + '">test</a>'

    if out != '':
        return out
    else:
        return 'no mikä ny'

def escape_values(bfo):
    """
    Called by BibFormat in order to check if output of this element
    should be escaped.
    """
    return 0
