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
"""BibFormat element - Prints abstract.
"""


import cgi


def format_element(bfo, limit="", max_chars="",
                   extension="[...] ", contextual="no",
                   highlight='no', escape="3",
                   separator="<br/>"):
    """ Prints the abstract of a record in HTML.
    """

    out = ''

    abstract = bfo.field('5208_a')
    if len(abstract) > 0 and abstract != "Abstract":
        print_extension = False
        if limit != "" and limit.isdigit():
            s_abstract = abstract.split(". ")
            if int(limit) < len(s_abstract):
                print_extension = True
                s_abstract = s_abstract[:int(limit)]
 
            out = '. '.join(s_abstract)
 
            if print_extension:
                out += " " + extension
        else:
             out += abstract

        if highlight == 'yes':
            out = bibformat_utils.highlight(out, bfo.search_pattern)
        return out
    else:
        return ""


def escape_values(bfo):
    """
    Called by BibFormat in order to check if output of this element
    should be escaped.
    """
    return 0
