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
"""BibFormat element - makes a prolog for CIP data
"""




import cgi
import re
def format_element(bfo, prefix, suffix):

    lang = ''    
    ilopub = ''
    en_prolog = 'ILO Cataloguing in Publication Data'
    es_prolog = 'Datos de catalogación en publicación de la OIT'
    fr_prolog = 'Données de catalogage avant publication du BIT'

    lang = bfo.field('998__a')    
    ilopub = bfo.field('992__a')    

    if lang.find('eng') > -1 and ilopub == 'ILO publication':
        return en_prolog
    elif lang.find('spa') > -1 and ilopub == 'ILO publication':
        return es_prolog
    elif lang.find('fre') > -1 and ilopub == 'ILO publication':
        return fr_prolog
    elif ilopub == 'ILO publication':
        return en_prolog
    else:
        return ''





