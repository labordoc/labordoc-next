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

"""
bfe_ILO_request_button.py Create button for requesting the item from old Labordoc
"""

import re

def format_element(bfo):
    
    # prepare variables
    voyager_sysno = bfo.field("970__a")
    voyager_sysno = re.sub('^LABORDOC-', '', voyager_sysno)
#    request_url = '''http://golf.ilo.org/cgi-bin/Pwebrecon.cgi?bbid=%s&BIB=%s&PAGE=REQUESTBIB" onclick="newWin(this.href); return false;''' % (voyager_sysno, voyager_sysno)
    request_url = '''http://ringo.ilo.org:7008/vwebv/patronRequests?&sk=en_ILO&bibId=%s" onclick="newWin(this.href); return false;''' % (voyager_sysno)


    # the html

    out_html ="""  
         <span class="RequestButton"> <a title="Request Button" href="%s"> Request <span class="RequestArrows">  &nbsp;&#187; </span> </a> </span> 
         """ % (request_url)
    return out_html
    
def escape_values(bfo):
    """
    Called by BibFormat in order to check if output of this element
    should be escaped.
    """
    return 0




