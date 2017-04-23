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

import json
import logging as log
import os
import sys
from argparse import ArgumentParser
from pathlib import Path
from time import sleep, time

from pymodoroi3 import Py3status


def main():
    log.basicConfig(
        level=log.INFO,
        format="[%(levelname)-8s] %(module)-15s - %(message)s",
    )

    args = parse_arguments()

    if args.daemon:
        while True:
            sleep(1 - time() % 1)
            handle_pymodoro_state()
    else:
        button = args.button_down
        if button:
            log.debug("Button '{}' pressed.".format(button))
            path = Path(args.session)
            if button == 1:
                log.debug("Starting session at '{}'.".format(path))
                path.touch()
            elif button == 3:
                log.debug("Stopping session at '{}'.".format(path))
                path.unlink()
    JSONOutput(full_text="\uf0ae").print()


def parse_arguments():
    """
    Parse the command line options.

    If no path to a Pymodoro session file is given, the application
    terminates with an error. The error message is forwarded to i3blocks
    prior to termination.

    """
    env = os.environ

    parser = ArgumentParser()
    parser.add_argument(
        '-v', '--version',
        action='version',
        version='%(prog)s v0.1.0'
    )
    parser.add_argument(
        "-s", "--session",
        default=env.get("BLOCK_INSTANCE"),
        help="Path to the Pymodoro session file. (default: Value of "
             "the 'BLOCK_INSTANCE' environment variable.)"
    )
    parser.add_argument(
        "-b", "--button",
        type=int,
        choices=(1, 3),
        dest="button_down",
        default=env.get("BLOCK_BUTTON") if env.get("BLOCK_BUTTON") else None,
        help="The (numeric) identifier of a pressed button. This "
             "option may be used to emulate user interaction. "
             "(default: Value of the 'BLOCK_BUTTON' environment variable.)"
    )
    parser.add_argument(
        "-d", "--daemon",
        action="store_true",
        help="Polls and prints the Pymodoro session state "
             "continuously, once per second.",
    )

    args, unknown = parser.parse_known_args()

    if not args.session and not args.daemon:
        JSONOutput(
            full_text="Argument Missing: Pymodoro session file path.",
            color="#ff0000"
        ).print()
        parser.print_help(file=sys.stderr)
        exit(1)

    return args


def handle_pymodoro_state():
    """Fetch the Pymodoro state and forward it to i3blocks."""
    pymodoro = Py3status()

    pymodoro.start_color = "#fefefe"
    pymodoro.end_color = "#e94d44"
    pymodoro.break_color = "#8bf09b"

    JSONOutput.from_pymodoro(pymodoro.pymodoro_main(None, None)).print()


class JSONOutput:
    """Class to generate output, compatible to the i3bar JSON protocol."""

    def __init__(self, full_text, color=None):
        super().__init__()
        self.full_text = full_text
        self.color = color

    def print(self):
        json.dump(self.__dict__, sys.stdout, ensure_ascii=False)
        sys.stdout.write("\n")
        sys.stdout.flush()

    @classmethod
    def from_pymodoro(cls, pymodoro_response):
        """
        Convert the output from Pymodoro to JSONOutput.

        Filters the given output to include only required elements. If
        the data suggests that no Pymodoro session is active, the result
        will hide the blocklet if it is forwarded to i3blocks.

        :param pymodoro_response: The received output from Pymodoro.
        :type pymodoro_response: dict
        :return: the converted output.
        :rtype: JSONOutput
        """
        result = cls(
            **{key: pymodoro_response[key] for key in (["full_text", "color"])}
        )

        if result.full_text == "-":
            result.full_text = ""
            result.separator = False
            result.separator_block_width = 0
        return result


if __name__ == "__main__":
    main()
