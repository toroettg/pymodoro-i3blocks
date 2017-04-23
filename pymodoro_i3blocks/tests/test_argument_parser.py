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

import sys
import unittest
from unittest.mock import patch

from pymodoro_i3blocks.pymodoro_i3blocks import parse_arguments


class TestArgumentParser(unittest.TestCase):
    @patch("pymodoro_i3blocks.pymodoro_i3blocks.os.environ.get", return_value=None, autospec=True)
    @patch("pymodoro_i3blocks.pymodoro_i3blocks.JSONOutput", autospec=True)
    def test_missing_session_path_output(self, i3printer_mock, _):
        """
        Test the behavior when the session parameter is missing.
        
        A descriptive message should be relayed to the blocklet, so that
        a user may quickly notice the error and is able to fix the
        problem.
        
        """
        with patch.object(sys, "argv", ["pymodoro-i3blocks"]), self.assertRaises(SystemExit):
            parse_arguments()
        i3printer_mock.assert_called_once_with(
            full_text="Argument Missing: Pymodoro session file path.",
            color="#ff0000"
        )

    @patch("pymodoro_i3blocks.pymodoro_i3blocks.os.environ.get", return_value=None, autospec=True)
    @patch("pymodoro_i3blocks.pymodoro_i3blocks.JSONOutput", autospec=True)
    def test_missing_session_path_termination(self, _, __):
        """Test whether the application terminates if the session parameter is missing."""
        with patch.object(sys, "argv", ["pymodoro-i3blocks"]), self.assertRaises(
                SystemExit) as context:
            parse_arguments()
        self.assertEqual(context.exception.code, 1)

    @patch("pymodoro_i3blocks.pymodoro_i3blocks.os.environ.get", return_value=None, autospec=True)
    @patch("pymodoro_i3blocks.pymodoro_i3blocks.JSONOutput", autospec=True)
    def test_missing_session_path_no_termination_daemon(self, _, __):
        """A missing session parameter for daemon mode is allowed."""
        with patch.object(sys, "argv", ["pymodoro-i3blocks", "--daemon"]):
            parse_arguments()

    @patch("pymodoro_i3blocks.pymodoro_i3blocks.os.environ.get",
           side_effect=lambda x: {"BLOCK_INSTANCE": "DUMMY", "BLOCK_BUTTON": "5"}.get(x),
           autospec=True)
    @patch("pymodoro_i3blocks.pymodoro_i3blocks.JSONOutput", autospec=True)
    def test_session_set_by_env(self, _, __):
        """Test whether the application sets the session parameter from an environment variable."""
        with patch.object(sys, "argv", ["pymodoro-i3blocks"]):
            self.assertEquals("DUMMY", parse_arguments().session)

    @patch("pymodoro_i3blocks.pymodoro_i3blocks.os.environ.get",
           side_effect=lambda x: {"BLOCK_INSTANCE": "DUMMY", "BLOCK_BUTTON": "5"}.get(x),
           autospec=True)
    @patch("pymodoro_i3blocks.pymodoro_i3blocks.JSONOutput", autospec=True)
    def test_button_down_set_by_env(self, _, __):
        """Test whether the application sets the button parameter from an environment variable."""
        with patch.object(sys, "argv", ["pymodoro-i3blocks"]):
            self.assertEquals(5, parse_arguments().button_down)

    @patch("pymodoro_i3blocks.pymodoro_i3blocks.os.environ.get",
           side_effect=lambda x: {"BLOCK_INSTANCE": "DUMMY"}.get(x), autospec=True)
    @patch("pymodoro_i3blocks.pymodoro_i3blocks.JSONOutput", autospec=True)
    def test_button_no_default(self, _, __):
        """Test whether the application sets no default value for the button parameter."""
        with patch.object(sys, "argv", ["pymodoro-i3blocks"]):
            self.assertEquals(None, parse_arguments().button_down)

    @patch("pymodoro_i3blocks.pymodoro_i3blocks.os.environ.get",
           side_effect=lambda x: {"BLOCK_INSTANCE": "DUMMY", "BLOCK_BUTTON": ""}.get(x),
           autospec=True)
    @patch("pymodoro_i3blocks.pymodoro_i3blocks.JSONOutput", autospec=True)
    def test_button_empty_default(self, _, __):
        """Test whether the application sets no empty string if the button parameter is not set."""
        with patch.object(sys, "argv", ["pymodoro-i3blocks"]):
            self.assertEquals(None, parse_arguments().button_down)


def get_suit():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestArgumentParser))
    return suite


if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(get_suit())
