# __init__.py -- The tests for selftest
# Copyright (C) 2012 Jelmer Vernooij <jelmer@samba.org>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; version 3
# of the License or (at your option) any later version of
# the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA  02110-1301, USA.

"""Tests for selftest."""

import unittest

def test_suite():
    result = unittest.TestSuite()
    names = ['socket_wrapper', 'target', 'testlist', 'run', 'samba']
    module_names = ['selftest.tests.test_' + name for name in names]
    loader = unittest.TestLoader()
    result.addTests(loader.loadTestsFromNames(module_names))
    return result
