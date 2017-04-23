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
from pathlib import Path
from unittest.mock import MagicMock, patch

from pymodoro_i3blocks.pymodoro_i3blocks import main


class TestMain(unittest.TestCase):
    @patch("pymodoro_i3blocks.pymodoro_i3blocks.parse_arguments",
           return_value=MagicMock(button_down=None, daemon=False), autospec=True)
    @patch("pymodoro_i3blocks.pymodoro_i3blocks.JSONOutput", autospec=True)
    def test_general(self, output_mock, _):
        main()
        output_mock.assert_called_once_with(full_text="\uf0ae")

    @patch("pymodoro_i3blocks.pymodoro_i3blocks.parse_arguments",
           return_value=MagicMock(session="DUMMY", daemon=False, button_down=1), autospec=True)
    @patch("pymodoro_i3blocks.pymodoro_i3blocks.JSONOutput", autospec=True)
    @patch("pymodoro_i3blocks.pymodoro_i3blocks.Path.touch", autospec=True)
    def test_recognize_session_start(self, touch_mock, _, __):
        """Test whether a left mouse click triggers starting / resetting the session."""
        main()
        touch_mock.assert_called_once_with(Path("DUMMY"))

    @patch("pymodoro_i3blocks.pymodoro_i3blocks.parse_arguments",
           return_value=MagicMock(session="DUMMY", daemon=False, button_down=3), autospec=True)
    @patch("pymodoro_i3blocks.pymodoro_i3blocks.JSONOutput", autospec=True)
    @patch("pymodoro_i3blocks.pymodoro_i3blocks.Path.unlink", autospec=True)
    def test_recognize_session_stop(self, unlink_mock, _, __):
        """Test whether a right mouse click triggers starting / resetting the session."""
        main()
        unlink_mock.assert_called_once_with(Path("DUMMY"))


def get_suit():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestMain))
    return suite


if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(get_suit())
