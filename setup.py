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

from setuptools import setup


def main():
    arguments = {
        "name":             "pymodoro-i3blocks",
        "version":          "0.1.0",

        "author":           "Tobias Röttger",
        "author_email":     "dev@roettger-it.de",
        "url":              "https://github.com/toroettg/pymodoro-i3blocks",

        "description":      "Displays and manages Pymodoro session states via i3blocks.",
        "long_description": _read_description(),

        "license":          "Apache License v2.0",
        "install_requires": _read_dependencies(),
        "dependency_links": _read_dependency_links(),
        "platforms":        ["any"],
        "classifiers":      _classifier,

        "entry_points":     {
            "console_scripts":
                ["pymodoro-i3blocks = pymodoro_i3blocks.pymodoro_i3blocks:main"]
        },

        "packages":         _modules,

        "test_suite":       "pymodoro_i3blocks.tests.test_runner"
    }

    setup(**arguments)


def _read_dependencies():
    dependencies = []
    with open("requirements.txt") as requirements:
        for line in requirements.readlines():
            module, version = line.split("==", 1)
            dependencies.append(module)
    return dependencies

def _read_dependency_links():
    with open("dependency-links.txt") as dependencies:
        dependency_links = dependencies.readlines()
    return dependency_links


def _read_description():
    with open("README.rst") as file:
        readme = file.read()
    with open("CHANGELOG.rst") as file:
        changelog = file.read()

    return readme + changelog

_modules = [
    'pymodoro_i3blocks',
]

_classifier = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: End Users/Desktop',
    'License :: OSI Approved :: Apache Software License',
    'Operating System :: POSIX :: Linux',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Topic :: Utilities '
]

if __name__ == "__main__":
    main()
