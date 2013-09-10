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

    # get series data

    series_title = ''
    series_data = ''
    pub_name = ''

    series_title = bfo.field('440%%a')    

    if len(series_title) > 0:
        series_title = re.sub(',$', '', series_title)
        series_title = re.sub(' ;$', '', series_title)
        series_title = re.sub('\.$', '', series_title)
    else:
        series_title = bfo.field('490%%a')
        if len(series_title) > 0: 
            series_title = re.sub(',$', '', series_title)
            series_title = re.sub(' ;$', '', series_title)
            series_title = re.sub('\.$', '', series_title)

    if series_title.find('paper')  > -1:
        series_title = re.sub('paper$', 'paper series', series_title)

    if series_title == "Document de travail" or series_title == "Working paper series" or series_title == "Documento de trabajo":
        pub_name = bfo.field('710%%b')
        if pub_name == '':
            pub_name = bfo.field('710%%a')
        if pub_name != '':
            series_title = series_title + ", " + pub_name

    if len(series_title) > 0:
        series_data =  'Publication-Status: Published in ' + series_title
        return series_data
    else: 
        series_data = ''








