# -*- coding: utf-8 -*-
##
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
Tag enricher tasklet.
Used at ILO to populate the 913__a tag used in Format facet.
"""

__revision__ = "$Id$"

import os
import ConfigParser
from tempfile import mkstemp
from datetime import datetime
from invenio.dbquery import run_sql
from invenio.intbitset import intbitset
from invenio.bibtask import task_update_progress
from invenio.config import CFG_ETCDIR, CFG_TMPDIR
from invenio.bibtask import write_message, task_low_level_submission
from invenio.search_engine import get_record, get_fieldvalues, perform_request_search


def create_marcxml_header():
    """
    Creates the MARC xml header
    @return: the marcxml header
    @rtype: string
    """
    marcxml_output = '<?xml version="1.0" encoding="UTF-8"?>\n'
    marcxml_output += '<collection xmlns="http://www.loc.gov/MARC21/slim">'
    return marcxml_output

def create_marcxml_footer():
    """
    Creates the MARC xml footer.
    @return: the marcxml footer
    @rtype: string
    """
    marcxml_output = '\n</collection>\n'
    return marcxml_output

def get_last_date():
    """
    Read from the file format_migration_last_run_date the date of the last
    time the tasklet run
    """
    file_path = CFG_TMPDIR + '/' + 'tag_enricher_last_run_date'
    # Let's read the last time the tasklet run
    if os.path.isfile(file_path):
        last_run_date_file = open(file_path, "r")
        if os.path.getsize(file_path) > 0:
            last_run_date = datetime.strptime(last_run_date_file.read(),"%Y-%m-%d %H:%M:%S")
            last_run_date_file.close()
        # It is the first iteration
        else:
            last_run_date = datetime.strptime("1900-01-01 00:00:00","%Y-%m-%d %H:%M:%S")
    else: # It is the first iteration
        last_run_date = datetime.strptime("1900-01-01 00:00:00","%Y-%m-%d %H:%M:%S")
    return last_run_date

def save_last_date(date=datetime.now()):
    file_path = CFG_TMPDIR + '/' + 'tag_enricher_last_run_date'
    last_run_date_file = open(file_path, "w")
    last_run_date_file.write(datetime.strftime(date, "%Y-%m-%d %H:%M:%S"))
    last_run_date_file.close()


def bst_format_tag_enricher():
    """
    Bibtasklet responsible of the generation of the 913__a tag used in Format facet.
    """
    task_update_progress("Started creating tags")
    write_message("Started creating tags")

    recids = run_sql("select id from bibrec where creation_date > %s", \
                              (get_last_date(), ))
    recids = [ result[0] for result in recids ]

    marcxml_output = create_marcxml_header()
    i = 0
    task_update_progress("Done %s of %s" % (i, len(recids)))
    for recid in recids:
        i += 1
        holdings = get_fieldvalues(recid, "964__d")
        fulltext = get_fieldvalues(recid, "8564_3")
        has_fulltext = False
        has_holdings = False

        record_xml = """<record>
                        <controlfield tag="001">%s</controlfield>
                        <datafield tag="913" ind1=" " ind2=" ">
                     """ % (str(recid),)

        for h in holdings:
            if not has_holdings and h in ('Book / article', 'Book (Historical collection)',
                                          'Reference material', 'Serial'):
                record_xml += """<subfield code="a">%s</subfield>""" % ("Physical copy")
                has_holdings = True

        for f in fulltext:
            if not has_fulltext and f.lower().find('text') >= 0:
                record_xml += """<subfield code="a">%s</subfield>""" % ("Electronic document")
                has_fulltext = True

        record_xml += "</datafield>  </record>"

        marcxml_output += record_xml
        task_update_progress("Done %s of %s" % (i, len(recids)))

    marcxml_output += create_marcxml_footer()
    write_message("Writting temporary file")
    current_date = datetime.now()
    file_path_fd, file_path_name = mkstemp(suffix='.xml',
                                           prefix="record_with_format_tag_%s" %
                                           current_date.strftime("%Y-%m-%d_%H:%M:%S"),
                                           dir=CFG_TMPDIR)
    os.write(file_path_fd, marcxml_output)
    os.close(file_path_fd)
    write_message("Submitting bibupload task")
    task_low_level_submission('bibupload', 'admin', '-a', '-c', file_path_name)

    save_last_date()

    write_message("Task finished")
    task_update_progress("Task finished")
