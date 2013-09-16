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
Create ranking for author alphabetic.
"""

__revision__ = "$Id$"


from invenio.dbquery import run_sql
import re

def chunk(input, size):
    return map(None, *([iter(input)] * size))

def author_descending(output_file):

    test_labordoc = re.compile('---')

    lquery100 = []
    lquery110 = []
    lquery111 = []
    lquery700 = []
    lquery710 = []
    lvbibid_query = []
    vbibid_100_700_110_710_111 = []
    vbibid_rankvalue = []

    query100 = run_sql("SELECT id_bibrec, value FROM bib10x, bibrec_bib10x WHERE tag LIKE '100%%a' AND id_bibxxx=id")
    query110 = run_sql("SELECT id_bibrec, value FROM bib11x, bibrec_bib11x WHERE tag LIKE '110%%a' AND id_bibxxx=id")
    query111 = run_sql("SELECT id_bibrec, value FROM bib11x, bibrec_bib11x WHERE tag LIKE '111%%a' AND id_bibxxx=id")
    query700 = run_sql("SELECT id_bibrec, value FROM bib70x, bibrec_bib70x WHERE tag LIKE '700%%a' AND id_bibxxx=id")
    query710 = run_sql("SELECT id_bibrec, value FROM bib71x, bibrec_bib71x WHERE tag LIKE '710%%a' AND id_bibxxx=id")
    vbibid_query = run_sql("SELECT id_bibrec, value FROM bib97x, bibrec_bib97x WHERE tag='970__a' AND id_bibxxx=id")

    # pretreatment, sort all queries

    for row in query100:
        lquery100.append(row[0])
        lquery100.append(row[1])

    query100_tuples = chunk(lquery100,2)
    query100_sorted_by_recid_tuples = sorted(query100_tuples, key=lambda tuple: tuple[0])

    for row in query110:
        lquery110.append(row[0])
        lquery110.append(row[1])

    query110_tuples = chunk(lquery110,2)
    query110_sorted_by_recid_tuples = sorted(query110_tuples, key=lambda tuple: tuple[0])

    for row in query111:
        lquery111.append(row[0])
        lquery111.append(row[1])

    query111_tuples = chunk(lquery111,2)
    query111_sorted_by_recid_tuples = sorted(query111_tuples, key=lambda tuple: tuple[0])

    for row in query700:
        lquery700.append(row[0])
        lquery700.append(row[1])

    query700_tuples = chunk(lquery700,2)
    query700_sorted_by_recid_tuples = sorted(query700_tuples, key=lambda tuple: tuple[0])

    for row in query710:
        lquery710.append(row[0])
        lquery710.append(row[1])

    query710_tuples = chunk(lquery710,2)
    query710_sorted_by_recid_tuples = sorted(query710_tuples, key=lambda tuple: tuple[0])

    for row in vbibid_query:
        lvbibid_query.append(row[0])
        lvbibid_query.append(row[1])

    vbibid_query_tuples = chunk(lvbibid_query,2)
    vbibid_sorted_by_recid_tuples = sorted(vbibid_query_tuples, key=lambda tuple: tuple[0])

    # unite

    vbibid_100_700_110_710_111.extend(query100_sorted_by_recid_tuples)
    vbibid_100_700_110_710_111.extend(query700_sorted_by_recid_tuples)
    vbibid_100_700_110_710_111.extend(query110_sorted_by_recid_tuples)
    vbibid_100_700_110_710_111.extend(query710_sorted_by_recid_tuples)
    vbibid_100_700_110_710_111.extend(query111_sorted_by_recid_tuples)

    all_sorted_by_recid_tuples = sorted(vbibid_100_700_110_710_111, key=lambda tuple: tuple[0])

    # delete not used

    del query100
    del query110
    del query111
    del query700
    del query710
    del query100_tuples
    del query110_tuples
    del query111_tuples
    del query700_tuples
    del query710_tuples
    del vbibid_query_tuples
    del lquery100[:]
    del lquery110[:]
    del lquery111[:]
    del lquery700[:]
    del lquery710[:]
    del lvbibid_query[:]
    del query100_sorted_by_recid_tuples
    del query700_sorted_by_recid_tuples
    del query110_sorted_by_recid_tuples
    del query710_sorted_by_recid_tuples
    del query111_sorted_by_recid_tuples
    del vbibid_100_700_110_710_111

    # make a dictionary using recid as key

    drecid = {}
    for k, v in all_sorted_by_recid_tuples:
        drecid.setdefault(k, []).append(v)

    # dictionary to list, join value lists and sort it according to authors

    drecid_list = []
    drecid_list = drecid.items()

    all_values = []

    for v in drecid_list:
        all_values.append(int(v[0]))
        all_values.append(" ".join(v[1]))

    all_tuples = chunk(all_values,2)
    all_tuples_sorted = sorted(all_tuples, key=lambda tuple: tuple[1].lower())

    # give sorted authors a ranking value starting from 999999

    author_ranked = []

    i = 999999
    for row in all_tuples_sorted:
        author_ranked.append(row[0])
        author_ranked.append(str(i))
        i = i - 1

    author_ranked_tuples = chunk(author_ranked,2)
    author_ranked_sorted_by_recid_tuples = sorted(author_ranked_tuples, key=lambda tuple: tuple[0])

    # deleting again unused dictionary and lists

    del drecid
    del drecid_list[:]
    del all_values[:]
    del all_tuples[:]
    del all_tuples_sorted[:]
    del author_ranked[:]
    del author_ranked_tuples[:]


    # Unite the result with dictionary key and print it with prolog

    vbibid_sorted_by_recid_tuples.extend(author_ranked_sorted_by_recid_tuples)

    drecid_final = {}

    for k, v in vbibid_sorted_by_recid_tuples:
        drecid_final.setdefault(k, []).append(v)

    drecid_list_final = []
    drecid_list_final = drecid_final.items()

    all_values_final = []

    for v in drecid_list_final:
        all_values_final.append("---".join(v[1]))

    f = open(output_file, 'w')
    for row in all_values_final:
        if test_labordoc.search(row):
            f.write(row + '\n')
    f.close()
