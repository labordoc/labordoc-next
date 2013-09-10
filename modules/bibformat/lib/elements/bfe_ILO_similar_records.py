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
"""BibFormat element - Prints titles with link to detailed record
"""
__revision__ = "$Id$"

def format_element(bfo):
    """
    Prints similar records link.

    @param separator: separator between the different titles
    @param highlight: highlights the words corresponding to search query if set to 'yes'
    """
    import cgi
    import re
    from invenio.urlutils import create_html_link
    #from websearch_templates import build_search_url
    from invenio.messages import gettext_set_language
    from invenio.config import CFG_SITE_URL
    import invenio.template
    websearch_templates = invenio.template.load('websearch')

    _ = gettext_set_language(bfo.lang)    # load the right message language
    recID = int(bfo.control_field('001')) 
    ln = bfo.lang
    #target = '<a href="%s/record/%s%s">'  % (CFG_SITE_URL, recid, lang)

    out = '<span class="moreinfo">%s</span>' % \
           create_html_link(websearch_templates.build_search_url(p="recid:%d" % recID,
                                                     rm="wrd",
                                                     ln=ln),
                                    {}, _("Similar records"),
                                    {'class': "none"})
    return out
    ## make a detailed record link
    #if len(edition_statement) > 0:
    #    return target + separator.join(titles) + "; " + edition_statement + "</a>"
    #else:
    #    return target + separator.join(titles) + "</a>"

def escape_values(bfo):
    """
    Called by BibFormat in order to check if output of this element
    should be escaped.
    """
    return 0






