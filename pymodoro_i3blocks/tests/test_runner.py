# =============================================================================
# -*- coding: utf-8 -*-
#
# Copyright (C) 2017 Tobias Röttger <dev@roettger-it.de>
#
# This file is part of pymodoro_i3blocks.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =============================================================================

import unittest

from pymodoro_i3blocks.tests import test_argument_parser, test_main


def get_suit():
    all_suites = unittest.TestSuite()

    suites = (
        test_main,
        test_argument_parser,
    )

    for suite in suites:
        all_suites.addTests(suite.get_suit())

    return all_suites


def load_tests(loader, tests, pattern):
    """Enable (graphical) unit testing for IDEs."""
    return get_suit()


if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(get_suit())
