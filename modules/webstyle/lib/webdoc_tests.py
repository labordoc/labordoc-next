# -*- coding: utf-8 -*-
## $Id$
##
## This file is part of CDS Invenio.
## Copyright (C) 2002, 2003, 2004, 2005, 2006, 2007, 2008 CERN.
##
## CDS Invenio is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 2 of the
## License, or (at your option) any later version.
##
## CDS Invenio is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with CDS Invenio; if not, write to the Free Software Foundation, Inc.,
## 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

"""WebDoc module unit tests."""

__revision__ = "$Id$"

import unittest

from invenio.config import CFG_SITE_LANGS
from invenio.testutils import make_test_suite, \
                              run_test_suite
from invenio.webdoc import transform

class WebDocLangTest(unittest.TestCase):
    """Check that WebDoc correctly supports <lang> translation directive"""

    def test_language_filtering(self):
        """webdoc - language filtering"""

        if 'en' not in CFG_SITE_LANGS:
            self.fail("SKIPPED: English language not configured, test skipped.")
        elif 'fr' not in CFG_SITE_LANGS:
            self.fail("SKIPPED: French language not configured, test skipped.")
        elif 'de' not in CFG_SITE_LANGS:
            self.fail("SKIPPED: German language not configured, test skipped.")

        result = transform('''
        <strong>
        <lang>
            <python>{}</python>
            <en><red>Book</red></en>
            <fr><yellow>Livre</yellow></fr>
            <de><blue>Buch</blue></de>
        </lang>
        </strong>
        ''', languages=['de'])

        self.assertEqual(result[0][0], 'de')
        self.assert_('<blue>Buch</blue>' in result[0][1])
        self.assert_('Livre' not in result[0][1])
        self.assert_('Book' not in result[0][1])

TEST_SUITE = make_test_suite(WebDocLangTest)

if __name__ == "__main__":
    run_test_suite(TEST_SUITE)