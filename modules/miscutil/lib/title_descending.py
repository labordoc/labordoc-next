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
publication_date_descending.py
Create ranking for title alphabetic descending.
"""

__revision__ = "$Id$"


from invenio.dbquery import run_sql
import re

def chunk(input, size):
    return map(None, *([iter(input)] * size))

def title_descending(output_file):
    title_cleaned = []
    vbibid_cleaned = []
    title_ranked = []
    title_year_ranked = []
    vbibid_rankvalue = []

    title_query = run_sql("SELECT id_bibrec, tag, value FROM bib24x, bibrec_bib24x WHERE tag LIKE '245%%a' AND id_bibxxx=id")
    vbibid_query = run_sql("SELECT id_bibrec, value FROM bib97x, bibrec_bib97x WHERE tag='970__a' AND id_bibxxx=id")

    # Clean, rank and sort the title query. First we find the second indicator, then
    # we move characters from the title beginning according to indicator value. After
    # the records are sorted using the shortened title and each record gets a ranking
    # value starting from .999999

    for row in title_query:
        title_cleaned.append(row[0])
        indicator = row[1]
        indicator = re.sub('^245.', '', indicator)
        indicator = re.sub('a$', '', indicator)
        title_cleaned.append(indicator)
        title_cleaned.append(row[2])
        sub_title = row[2]
        if sub_title != '' and indicator != '' and indicator.isdigit():
            sub_title = sub_title[int(indicator):]
            sub_title = sub_title.lstrip()
            title_cleaned.append(sub_title)
        else:
            title_cleaned.append(sub_title)

    title_cleaned_tuples = chunk(title_cleaned,4)
    title_sorted_by_choppedtitle_tuples = sorted(title_cleaned_tuples, key=lambda tuple: tuple[3].lower())


    i = 999999
    for row in title_sorted_by_choppedtitle_tuples:
        title_ranked.append(row[0])
        title_ranked.append(row[2])
        title_ranked.append(str(i))
        i = i - 1

    title_ranked_tuples = chunk(title_ranked,3)
    title_sorted_by_recid_tuples = sorted(title_ranked_tuples, key=lambda tuple: tuple[0])


    # The record id is changed to 970__a old labordoc value, to be
    # able to find a record later with the single_tag_ranking method.
    # Make tuples and sort first to be sure...

    for row in vbibid_query:
        vbibid_cleaned.append(row[0])
        vbibid_cleaned.append(row[1])

    vbibid_cleaned_tuples = chunk(vbibid_cleaned,2)
    vbibid_sorted_by_recid_tuples = sorted(vbibid_cleaned_tuples, key=lambda tuple: tuple[0])


    x = 0
    y = 0
    for vbibid_row in vbibid_sorted_by_recid_tuples:
        #y = y + 1
        #print y
        not_found = True
        recid_vbibid = vbibid_row[0]
        for title_row in title_sorted_by_recid_tuples:
            recid_title = title_row[0]
            x = x + 1
            if recid_title == recid_vbibid:
                not_found = False
                vbibid_rankvalue.append(vbibid_row[1])
                vbibid_rankvalue.append(title_row[2])
                del title_sorted_by_recid_tuples[0:x]
                x = 0
                break
        if not_found:
            vbibid_rankvalue.append('not found')
            vbibid_rankvalue.append('not found')
            x = 0

    vbibid_rankvalue_tuples = chunk(vbibid_rankvalue,2)

    f = open(output_file, 'w')

    for row in vbibid_rankvalue_tuples:
        recid_rankvalue = str(row[0]) + '---' + str(row[1])
        f.write(recid_rankvalue + '\n')

    f.close()
