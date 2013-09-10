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
"""BibFormat element - Prints 110a and 710a field information for CIP data
"""




import cgi
import re
def format_element(bfo, prefix, suffix, separator="; "):

    editors_1 = '' 
    editors_2 = ''
    editors_3 = ''
    editors_4 = ''
    entries = []
    entry_1 = bfo.fields('110%%')
    entry_2 = bfo.fields('710%%')
    entry_3 = bfo.fields('111%%')
    entry_4 = bfo.fields('711%%')


    #entries.extend(entry_1)
    #entries.extend(entry_2)
    #entries.extend(entry_3)
    #entries.extend(entry_4)

    

    #for entry in entries:
    #   if entry.has_key('a'):
    #        if entry['a'][-1] == '.':
    #            entry['a'] = entry['a'][:-1]

    for entry in entry_1:
       if entry.has_key('a'):
            if entry['a'][-1] == '.':
                entry['a'] = entry['a'][:-1]
            editors_1 = entry['a']  
       if entry.has_key('b'):
            editors_1 = editors_1 + ' ' + entry['b']  
       if entry.has_key('n'):
            editors_1 = editors_1 + ' ' + entry['n']
       if entry.has_key('d'):
            editors_1 = editors_1 + ' ' + entry['d']
       if entry.has_key('c'):
            editors_1 = editors_1 + ' ' + entry['c']

    for entry in entry_2:
       if entry.has_key('a'):
            if entry['a'][-1] == '.':
                entry['a'] = entry['a'][:-1]
            editors_2 = entry['a']  
       if entry.has_key('b'):
            editors_2 = editors_2 + ' ' + entry['b']
       if entry.has_key('n'):
            editors_2 = editors_2 + ' ' + entry['n']
       if entry.has_key('d'):
            editors_2 = editors_2 + ' ' + entry['d']
       if entry.has_key('c'):
            editors_2 = editors_2 + ' ' + entry['c']

    for entry in entry_3:
       if entry.has_key('a'):
            if entry['a'][-1] == '.':
                entry['a'] = entry['a'][:-1]
            editors_3 = entry['a']
       if entry.has_key('b'):
            editors_3 = editors_3 + ' ' + entry['b']
       if entry.has_key('n'):
            editors_3 = editors_3 + ' ' + entry['n']
       if entry.has_key('d'):
            editors_3 = editors_3 + ' ' + entry['d']
       if entry.has_key('c'):
            editors_3 = editors_3 + ' ' + entry['c']

    for entry in entry_4:
       if entry.has_key('a'):
            if entry['a'][-1] == '.':
                entry['a'] = entry['a'][:-1]
            editors_4 = entry['a']
       if entry.has_key('b'):
            editors_4 = editors_4 + ' ' + entry['b']
       if entry.has_key('n'):
            editors_4 = editors_4 + ' ' + entry['n']
       if entry.has_key('d'):
            editors_4 = editors_4 + ' ' + entry['d']
       if entry.has_key('c'):
            editors_4 = editors_4 + ' ' + entry['c']


    if editors_1 != '':        
        entries.append(editors_1)
    if editors_2 != '':        
        entries.append(editors_2)
    if editors_3 != '':        
        entries.append(editors_3)
    if editors_4 != '':        
        entries.append(editors_4)


    nb_entries = len(entries)


    if nb_entries > 0:
        all_entries = separator.join(entries)
        return all_entries
    else:
        return ''    


