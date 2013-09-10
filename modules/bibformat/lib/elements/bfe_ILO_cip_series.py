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
"""BibFormat element - Prints series fields information for CIP data
"""


import cgi
import re
def format_element(bfo, prefix, suffix):

    series_title = ''
    series_editors = ''
    issn = ''    

    series_title = bfo.field('440%%a')    
    series_editors = bfo.field('440%%v')    
    issn = bfo.field('440%%x')    

    if len(series_title) > 0:
        series_title = re.sub(',$', '', series_title)
        series_title = re.sub(' ;$', '', series_title)
        series_title = ' (' + series_title  
    else:
        series_title = bfo.field('490%%a')
        if len(series_title) > 0: 
            series_title = re.sub(',$', '', series_title)
            series_title = re.sub(' ;$', '', series_title)
            series_title = ' (' + series_title  

    if len(series_editors) > 0:
        series_editors = ' ; ' + series_editors  
    else:
        series_editors = bfo.field('490%%v')
        if len(series_editors) > 0:
            series_editors = ' ; ' + series_editors

    if len(issn) > 0:
        issn = re.sub(' ;$', '', issn)
        issn = ', ISSN: ' + issn  

    if len(series_title) > 0:
        series_data = series_title + series_editors + issn + ')'
        return series_data
    else:
        return ''








