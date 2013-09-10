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
"""BibFormat element - Prints link to article via sfx
"""




import cgi
import re
from invenio.urlutils import create_html_link
#from invenio.messages import gettext_set_language
from invenio.config import CFG_SITE_URL
def format_element(bfo, prefix, suffix):


#    SFX_SITE_URL = 'http://sfxhostedeu.exlibrisgroup.com/41ILO?sid=labordoc'     
#
#
#    aufirst = bfo.field('100%%a')    
#    aufirst = re.sub("^.*, ", "", aufirst)
#    aufirst = re.sub("\.$", "", aufirst)
#    aulast = bfo.field('100%%a')    
#    aulast = re.sub(", .*$", "", aulast)
#    atitle = bfo.field('245%%a')    
#    atitle = atitle.replace("\"", "%22")
#    atitle = atitle.replace("\'", "%27")
#    atitle = re.sub(" */$", "", atitle)
#    atitle = atitle.replace(" ", "+")
#    title = bfo.field('773%%t')    
#    title = re.sub("\.$", "", title)
#    title = title.replace(" ", "+")
#    volume = bfo.field('773%%g') 
#    if 'Vol.' in volume:
#        volume = re.sub("^Vol\. ", "", volume)
#        volume = re.sub(", .*$", "", volume)
#    else:
#        volume = ''
#    issue = bfo.field('773%%g')    
#    issue = re.sub(".* no\. ", "", issue) # gNo. 12 (ene. 2012)
#    issue = re.sub("^No\. ", "", issue) # gNo. 12 (ene. 2012)
#    issue = re.sub(" .*$", "", issue)
#    date = bfo.field('997__a')    
#    spage = bfo.field('300%%a')    
#    spage = re.sub("^p\. ", "", spage)
#    spage = re.sub("-.*$", "", spage)
#    spage = re.sub(" :$", "", spage)
#    spage = re.sub("p\.$", "", spage)
#    spage = re.sub(" *$", "", spage)
#    issn = bfo.field('773%%x')    
   

    SFX_SITE_URL = 'http://sfxhostedeu.exlibrisgroup.com/41ILO?ctx_enc=info%3Aofi%2Fenc%3AUTF-8'
    SFX_SITE_URL_END ='&ctx_ver=Z39.88-2004&rfr_id=info%3Asid%2Fsfxit.com%3Acitation&rft.genre=article'     
    SFX_SITE_URL = SFX_SITE_URL + SFX_SITE_URL_END

    atitle = bfo.field('245%%a')    
    atitle = atitle.replace("\"", "%22")
    atitle = atitle.replace("\'", "%27")
    atitle = re.sub(" */$", "", atitle)
    atitle = atitle.replace(" ", "%20")
    jtitle = bfo.field('773%%t')    
    jtitle = re.sub("\.$", "", jtitle)
    jtitle = jtitle.replace(" ", "%20")
    volume = bfo.field('773%%g') 
    if 'Vol.' in volume:
        volume = re.sub("^Vol\. ", "", volume)
        volume = re.sub(", .*$", "", volume)
    else:
        volume = ''
    issue = bfo.field('773%%g')
    issue = re.sub(".* no\. ", "", issue) 
    issue = re.sub(".* No\. ", "", issue) 
    issue = re.sub("^No\. ", "", issue) 
    issue = re.sub(" .*$", "", issue)  
    spage = bfo.field('300%%a')    
    epage = spage
    spage = re.sub("^p\. ", "", spage)
    spage = re.sub("-.*$", "", spage)
    spage = re.sub(" :$", "", spage)
    spage = re.sub("p\.$", "", spage)
    spage = re.sub(" *$", "", spage)

    if '-' in epage:
        epage = re.sub("^p.*-", "", epage)
        epage = re.sub(" .*$", "", epage)
    else:
        epage = spage

    issn = bfo.field('773%%x')    

    target = '<a href="%s&rft.atitle=%s&rft.jtitle=%s&rft.spage=%s&rft.epage=%s&volume=%s&issue=%s&issn=%s">' \
                       % (SFX_SITE_URL, atitle, jtitle, spage, epage, volume, issue, issn)
    text = 'Check for Fulltext'

    if 'Conf' not in jtitle and jtitle != '':
        return target + text  + "</a>" # + '|' + epage + '|'
    else:
        return ''

def escape_values(bfo):
    """
    Called by BibFormat in order to check if output of this element
    should be escaped.
    """
    return 0
