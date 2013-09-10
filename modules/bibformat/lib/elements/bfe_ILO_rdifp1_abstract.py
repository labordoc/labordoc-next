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
"""BibFormat element - Prints English and French abstract.
"""

from textwrap import wrap
import cgi
def format_element(bfo, prefix, suffix):

    all_abstract = ''
    abstract = bfo.field('5208_a')
    out = '''
        %s 
    ''' % abstract

    if len(abstract) > 0 and abstract != "Abstract":
        all_abstract = 'Abstract: ' + abstract
        all_abstract = '\n'.join(['\n '.join(wrap(block, width=80)) for block in all_abstract.splitlines()])
        return all_abstract
    else:
        return ''

def escape_values(bfo):
    """
    Called by BibFormat in order to check if output of this element
    should be escaped.
    """
    return 0
