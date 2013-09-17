# -*- coding: utf-8 -*-
## This file is part of Invenio.
## Copyright (C) 2013 CERN.
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
Labordoc local customization of Flask application
"""

from flask import current_app

def customize_app(app):

    del app.config['menubuilder_map']['main'].children['webdeposit']

    Menu = type(app.config['menubuilder_map']['main'])

    # menu for resources
    resources = Menu('main.resources', 'Resources', '', 2)
    app.config['menubuilder_map']['main'].children['resources'] = resources
    resources.children = {}
 
    resources_links = {'ILO Library': 'http://www.ilo.org/public/english/support/lib/index.htm',
                      'ILO Databases': 'http://www.ilo.org/public/english/support/lib/resource/ilodatabases.htm',
                      'ILO Thesaurus': 'http://www.ilo.org/thesaurus/defaulten.asp',
                      'Resource Guides': 'http://www.ilo.org/public/english/support/lib/resource/guides.htm',
                      'E-Journals': 'http://sfxhostedeu.exlibrisgroup.com/41ILO/az',
                      'MultiSearch': 'http://ilo.deepwebaccess.com/ilo/search.html'}
 
    i = 0
    for k, v in resources_links.items():
        resources.children[k] = Menu('main.resources.'+k, k,
                                       v, i)
        i += 1

    # menu for help
    help = Menu('main.help', 'Help', '', 3)
    app.config['menubuilder_map']['main'].children['help'] = help
    help.children = {}
 
    help_links = {'Ask a Librarian': 'mailto:informs@ilo.org?subject=Ask a Librarian',
                  'Search Tips': 'http://labordoc.ilo.org/help/search-tips'}
 
    i = 0
    for k, v in help_links.items():
        help.children[k] = Menu('main.help.'+k, k,
                                v, i)
        i += 1

    # menu for ask_librarian
    about = Menu('main.about', 'About Labordoc', \
                 'http://www.ilo.org/public/english/support/lib/labordoc/index.htm', 9999)
    app.config['menubuilder_map']['main'].children['about'] = about
