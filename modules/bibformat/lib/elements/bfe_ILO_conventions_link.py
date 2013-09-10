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
#<BFE_ILO_CONVENTIONS prefix='<br/><small class="quicknote">' suffix="</small>"
#
## You should have received a copy of the GNU General Public License
## along with Invenio; if not, write to the Free Software Foundation, Inc.,
## 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.
"""BibFormat element - Prints link to ILO convention collections
"""




import cgi
import re
from invenio.urlutils import create_html_link
#from invenio.messages import gettext_set_language
from invenio.config import CFG_SITE_URL
def format_element(bfo, prefix, suffix):


    conv = bfo.field('970__a')    
    convno = bfo.field('980__n')
    lang = bfo.lang
    target = '<a href="%s/search?jrec=1&ln=%s&cc=%s">'  % (CFG_SITE_URL, lang, convno)
    text = 'More background documents on ' + convno

    if conv.startswith('ILOCONV') and len(convno) > 0:
        return target + text  + "</a>"
    else:
        return ''

def escape_values(bfo):
    """
    Called by BibFormat in order to check if output of this element
    should be escaped.
    """
    return 0
