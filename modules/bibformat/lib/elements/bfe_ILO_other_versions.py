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
"""BibFormat element - Prints imprint publication date
"""
__revision__ = "$Id$"

import cgi
import re
from urllib import quote
from invenio.config import CFG_SITE_URL
from invenio.websubmit_functions.Create_Modify_Interface import Create_Modify_Interface_getfieldval_fromDBrec
from invenio.bibupload import find_record_from_sysno
#value =  Create_Modify_Interface_getfieldval_fromDBrec('8564_u',440333)
#value = find_record_from_sysno('LABORDOC-447053')

def format_element(bfo, separator="<br/>"):
    """
    Prints the other language versions of the document. First get old sysno's 
    and use those to retrieve the regid. Then print title of the other versions.
    """
    out = ''    
    temp = ''
    temp2 = ''
    voyager_sysno_with_label = []
    recids = []
    title = ''    
    title_remainder = ''
    other_version_titles = []
    url = ''

    voyager_sysno = bfo.fields("7750_w")

    for sysno in voyager_sysno:
        temp += 'LABORDOC-'
        temp += sysno
        voyager_sysno_with_label.append(temp)
        temp = ''
     
    for sysno_with_label in voyager_sysno_with_label:
        temp2 = find_record_from_sysno(sysno_with_label)
        recids.append(temp2)

    for recid in recids:
        if recid:

            if len(title) == 0:
                title = Create_Modify_Interface_getfieldval_fromDBrec('245%%a',recid)
                title_remainder = Create_Modify_Interface_getfieldval_fromDBrec('245%%b',recid)

            if len(title) != 0:
                if not "DELETED" in title:
                    if title_remainder:
                        title += ': ' + title_remainder
                        title = title.replace('::', ':')
                    title = re.sub('/$', '', title)
                    title = re.sub(':$', '', title)
                    title = re.sub(' : ', ': ', title)
                    #url = '<a href="' + CFG_SITE_URL + '/search?recid=%d' % (recid, )
                    url = '<a href="' + CFG_SITE_URL + '/record/%d' % (recid, )
                    #url +=             '&amp;ln=%s' % (bfo.lang, )
                    url +=             '?ln=%s' % (bfo.lang, )
                    url +=             '">%s</a>' % (title, )
                    other_version_titles.append(url)
                    url = ''
            title = ''
            title_remainder = ''
       
    if other_version_titles:
        out = separator.join(other_version_titles)
    if out != '':
        return out

def escape_values(bfo):
    """
    Called by BibFormat in order to check if output of this element
    should be escaped.
    """
    return 0
