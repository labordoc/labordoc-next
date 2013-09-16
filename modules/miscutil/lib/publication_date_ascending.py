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
Create ranking for year descending and title alphabetic.
"""

__revision__ = "$Id$"


from invenio.dbquery import run_sql
import re
import subprocess
import datetime

def chunk(input, size):
    return map(None, *([iter(input)] * size))

def publication_date_ascending(output_file):

#test_year = re.compile('^[1-20-90-90-9]+$')
    test_year = re.compile('^[12][0-9]{3}$')

    year_cleaned = []
    year_rank_values = []
    title_cleaned = []
    vbibid_cleaned = []
    title_ranked = []
    title_year_ranked = []
    join_title_year = []
    vbibid_rankvalue = []

    year_query = run_sql("SELECT id_bibrec, value FROM bib99x, bibrec_bib99x WHERE tag='997__a' AND id_bibxxx=id")
    title_query = run_sql("SELECT id_bibrec, tag, value FROM bib24x, bibrec_bib24x WHERE tag LIKE '245%%a' AND id_bibxxx=id")
    vbibid_query = run_sql("SELECT id_bibrec, value FROM bib97x, bibrec_bib97x WHERE tag='970__a' AND id_bibxxx=id")

# Clean, rank and sort the year query. Each record will get simply a value according to year.
# If year format is wrong, then value is 0.

    now = datetime.datetime.now()
    current_year = now.year


    for row in year_query:
        year_cleaned.append(row[0])
        if test_year.match(row[1]) and current_year >= int(row[1]):
            year_cleaned.append(row[1])
        else:
            year_cleaned.append('0')

    year_cleaned_tuples = chunk(year_cleaned,2)
    year_sorted_by_year_tuples = sorted(year_cleaned_tuples, key=lambda tuple: tuple[1], reverse=True)

# Since this will be in ascending year order, calculate a value for it

    for row in year_sorted_by_year_tuples[0:1]:
        start_year = row[1]

    i = 1
    for row in year_sorted_by_year_tuples:
        row_year = row[1]
        if start_year == row_year:
            year_rank_value = int(start_year) - int(row_year) + int(row_year) + int(i)
            year_rank_values.append(row[0])
            year_rank_values.append(year_rank_value)
            check_year = row[1]
        elif row_year < start_year and check_year != row_year:
            i = i + 1
            year_rank_value = int(start_year) - int(row_year) + int(row_year) + int(i)
            year_rank_values.append(row[0])
            year_rank_values.append(year_rank_value)
            check_year = row[1]
        else:
            year_rank_values.append(row[0])
            year_rank_values.append(year_rank_value)


    year_rank_values_tuples = chunk(year_rank_values,2)
    year_sorted_by_recid_tuples = sorted(year_rank_values_tuples, key=lambda tuple: tuple[0])

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
        title_ranked.append('.' + str(i))
        i = i - 1

    title_ranked_tuples = chunk(title_ranked,3)
    title_sorted_by_recid_tuples = sorted(title_ranked_tuples, key=lambda tuple: tuple[0])

# The year and title records are compined and ranking values are added

    x = 0
    for year_row in year_sorted_by_recid_tuples:
        not_found = True
        recid_year = year_row[0]
        for title_row in title_sorted_by_recid_tuples:
            recid_title = title_row[0]
            x = x + 1
            if recid_title == recid_year:
                not_found = False
                title_year_ranked.append(year_row[0])
                #title_year_ranked.append(title_row[0])
                #title_year_ranked.append(title_row[1])
                #title_year_ranked.append(year_row[1])
                #title_year_ranked.append(title_row[2])
                title_year_ranked.append(str(year_row[1]) + (title_row[2]))
                del title_sorted_by_recid_tuples[0:x]
                x = 0
                break
        if not_found:
            title_year_ranked.append(year_row[0])
            #title_year_ranked.append('not found')
            #title_year_ranked.append('not found')
            #title_year_ranked.append(year_row[1])
            #title_year_ranked.append('not found')
            title_year_ranked.append(str(year_row[1]))
            x = 0

    title_year_ranked_tuples = chunk(title_year_ranked,2)

# The record id is changed to 970__a old labordoc value, to be
# able to find a record later with the single_tag_ranking method.
# Make tuples and sort first to be sure...

    for row in vbibid_query:
        vbibid_cleaned.append(row[0])
        vbibid_cleaned.append(row[1])

    vbibid_cleaned_tuples = chunk(vbibid_cleaned,2)
    vbibid_sorted_by_recid_tuples = sorted(vbibid_cleaned_tuples, key=lambda tuple: tuple[0])


    x = 0
    for vbibid_row in vbibid_sorted_by_recid_tuples:
        not_found = True
        recid_vbibid = vbibid_row[0]
        for title_row in title_year_ranked_tuples:
            recid_title = title_row[0]
            x = x + 1
            if recid_title == recid_vbibid:
                not_found = False
                vbibid_rankvalue.append(vbibid_row[1])
                vbibid_rankvalue.append(title_row[1])
                del title_year_ranked_tuples[0:x]
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
