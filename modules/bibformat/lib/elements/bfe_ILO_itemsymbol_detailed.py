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
BibFormat element - Prints item symbol or cover image.
"""

from invenio.config import CFG_SITE_URL
import cgi
import string
import re
import os.path
import urllib2

def format_element(bfo):
    """
    Item type icon
    """

    # hard-code
    CFG_LABORDOC_URL = "http://labordoc.ilo.org"

    isbns = []    
    baseurl = CFG_SITE_URL + '/img/'
    conv = bfo.field('970__a')
    convt = bfo.field('980__c')
    isbns = bfo.fields('020%%a')
    urls = bfo.fields('8564_u')
    gb1  = bfo.field('1102_b')
    ic1  = bfo.field('1112_a')
    wp1  = bfo.field('440_0a')
    wp2  = bfo.field('4900_a')
    wp3  = bfo.field('4901_a')
    ic2  = bfo.field('655_7a')
    gb2  = bfo.field('7102_a')
    gb3  = bfo.field('7102_b')
    gb4  = bfo.field('7112_a')
    out = ""
    isbn = ""
    nb_isbns = len(isbns)

    # conventions
    if conv.startswith('ILOCONV'):
        if convt.startswith('Discus'):
            out = '<div class="convIteml">DP</div>'
        if convt.startswith('Documen') or convt.startswith('Preparatory docu'):
            out = '<div class="convIteml">Pre</div>'
        if convt.startswith('Informe') or convt.startswith('Report') or convt.startswith('Rappor'):
            out = '<div class="convItem">Com</div>'
        if convt.startswith('List'):
            out = '<div class="convIteml">LP</div>'
        if convt.startswith('Recom'):
            out = '<div class="convIteml">Rec</div>'
        if convt.startswith('Resolu') or convt.startswith('Résolut'):
            out = '<div class="convIteml">Res</div>'
        if convt.startswith('Text'):
            out = '<div class="convIteml">T</div>'
        if convt.startswith('Vot'):
            out = '<div class="convIteml">V</div>'
        return out
    
    test_ic_gb = gb1 + ' ' + gb2 + ' ' + gb3 + ' ' + gb4 + ' ' + ic1 + ' ' + ic2
    test_wp = wp1 + ' ' + wp2 + ' ' + wp3 
    item_type = bfo.field('996__a')

    imagepath2 = ''
    test = ''

    for url in urls:
        if url.find('.pdf') > -1 and url.find('libdoc') > -1:
            test = ''.join(url.split('/')[-1:])
            test = re.sub('.pdf','', test)
            imagepath2 = '/opt/invenio/var/www/img/cover/' + test + '-M.jpg'
            break

    for isbntest in isbns:
        isbn = isbntest
        isbn = re.sub(' .*','', isbn)
        imagepath = '/opt/invenio/var/www/img/cover/' + isbn + '-M.jpg'
#         if os.path.isfile(imagepath): sudo ln -s /opt/invenio/var/www/img/cover /data01/invenio-data/cover
        imageurl = CFG_LABORDOC_URL + '/img/cover/' + isbn + '-M.jpg'
        try:
            f = urllib2.urlopen(urllib2.Request(imageurl))
            image_exists = True
        except:
            image_exists = False

        if image_exists:       
            out = '''<img class="detailsImageCover" src="%s">''' % imageurl
            return out
    
#     if os.path.isfile(imagepath2): sudo ln -s /opt/invenio/var/www/img/cover /data01/invenio-data/cover
    try:
        f = urllib2.urlopen(urllib2.Request(imagepath2))
        image_exists = True
    except:
        image_exists = False

    if image_exists:
        imageurl = CFG_LABORDOC_URL + '/img/cover/' + test + '-M.jpg'
        out = '''<img class="detailsImageCover" src="%s">''' % imageurl
        return out

    else:
        if item_type == "am":
            if test_ic_gb.find('conference') >= 1 or test_ic_gb.find('Governing body') >= 1 or test_ic_gb.find('International Labour Conference') >= 1:
                item_type_new = "empty"
            elif test_wp.find('working paper') >= 1 or test_wp.find('document de travail') >= 1 or test_wp.find('documento de trabajo') >= 1:
                item_type_new = baseurl + "empty.gif"
            else: 
                item_type_new = "empty"
        
        elif item_type == "as" or item_type == "aa":
            if test_ic_gb.find('conference') >= 1 or test_ic_gb.find('Governing body') >= 1 or test_ic_gb.find('International Labour Conference') >= 1:
                item_type_new = "empty"
            else: 
                item_type_new = "empty"
    
        elif item_type == "gm" or item_type == "mm" or item_type == "cm":
            item_type_new = "empty"
        else:
            item_type_new = "empty"
       
        if item_type_new:
            if isbn != '' and item_type_new != 'empty':
                out = '''<img class="detailsImageCover" src='http://covers.openlibrary.org/b/isbn/%s-S.jpg?default=false' onerror="this.src='%s';">''' % (isbn, item_type_new)
                return out
            else:
                return ""
        else:
            return ""


def escape_values(bfo):
    """
    Called by BibFormat in order to check if output of this element
    should be escaped.
    """
    return 0
