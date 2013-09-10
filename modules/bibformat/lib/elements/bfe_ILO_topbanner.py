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
BibFormat element - Prints HTML topbanner with category, rep. number, etc.
"""


import cgi
import string
import re

def format_element(bfo, separator=" ", highlight='no'):
    """
    HTML top page banner containing category, rep. number, etc
    """



    gb1 = bfo.field('1102_b')
    ic1 = bfo.field('1112_a')
    wp1 = bfo.field('440_0a')
    wp2 = bfo.field('4900_a')
    wp3 = bfo.field('4901_a')
    ic2 = bfo.field('655_7a')
    gb2 = bfo.field('7102_a')
    gb3 = bfo.field('7102_b')
    gb4 = bfo.field('7112_a')
# fix in search
#655_7a:'ILO_pub' or 655_7a:'OIT pub' or author:'international labour office' or author:'international labour organization' or author:'international #labour organisation' or author:'international labour conference' or  author:ilo or author:oit or author:bit or author:'governing body'



    test_ic_gb = gb1 + ' ' + gb2 + ' ' + gb3 + ' ' + gb4 + ' ' + ic1 + ' ' + ic2
    test_wp = wp1 + ' ' + wp2 + ' ' + wp3 
    item_type = bfo.field('996__a')


    if item_type == "am":
        if test_ic_gb.find('conference') >= 1 or test_ic_gb.find('Governing body') >= 1 or test_ic_gb.find('International Labour Conference') >= 1:
            item_type_new = "Conference document"
        elif test_wp.find('working paper') >= 1 or test_wp.find('document de travail') >= 1 or test_wp.find('documento de trabajo') >= 1:
            item_type_new = "Working paper"
        else: 
            item_type_new = "Book"
        
    if item_type == "as" or item_type == "aa":
        if test_ic_gb.find('conference') >= 1 or test_ic_gb.find('Governing body') >= 1 or test_ic_gb.find('International Labour Conference') >= 1:
            item_type_new = "Conference document"
        else: 
            item_type_new = "Article / Periodical"

    if item_type == "gm" or item_type == "mm" or item_type == "cm":
        item_type_new = "Multimedia"




    out = '''
         %s
    ''' % item_type_new

  #  if item_type_new:
    return out
  #  else:
  #      return ''


