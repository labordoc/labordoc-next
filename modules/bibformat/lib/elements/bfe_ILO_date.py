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
"""BibFormat element - Prints imprint publication date
"""
__revision__ = "$Id$"

# if type as and 3620_ $$a exists then take year from 362 a (including the -)

import time

def format_element(bfo, date_format='%d %B %Y'):
    """
    Prints the imprint publication date. If <code>format</code> is specified,
    Parameter <code>date_format</code> allows to specify the string representation of the output.
    The format string has the same behaviour as the strftime() function.
    <pre>Eg: 1982-09-24 07:32:00
        "%d %B %Y"   -> 24 September 1982
        "%I:%M"      -> 07:32
    </pre>
    @see: pagination.py, publisher.py, reprints.py, imprint.py, place.py
    @param date_format date format

    For ILO purpose, check if the record is periodical with year hyphen. eg. 2008-
    """

    doctype = bfo.field('996__a')
    date_as = bfo.field('3620_a')
    #date_as = bfo.field('866%%a')
    #info_as = bfo.field('866%%z')
    date = bfo.field('997__a')
    if doctype == 'as' and date_as != '':
        #date_as = date_as + ' ' + info_as
        return date_as
    elif date_format != '':
        try:
            date_time = time.strptime(date, "%Y-%m-%d")
            return time.strftime(date_format, date_time)
        except ValueError:
            return date
    else:
        return date

