#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Fabric file for development use.
"""

import os
import sys

from fabric.api import local
from fabric.contrib import django


def start():
    """
    Starts OpenSlides installed in the python path.

    At the moment passing additional args to OpenSlides is not possible.
    """
    sys.path.insert(0, '')
    from openslides.main import main
    sys.argv.remove('start')
    main()


def pep8():
    """
    Checks for PEP 8 errors in openslides_csv_export and in tests.
    """
    local('pep8 --max-line-length=150 --statistics openslides_csv_export')
    local('pep8 --max-line-length=150 --statistics tests')


def test(module='tests'):
    """
    Runs the unit tests.
    """
    from django.core import management
    sys.path.insert(0, '')
    django.settings_module('tests.settings')
    sys.argv.pop()
    sys.argv.extend(['test', module])
    management.execute_from_command_line()


def prepare_commit():
    """
    Does everything that should be done before a commit.

    At the moment it is running the tests and checks for PEP 8 errors.
    """
    test()
    pep8()


def travis_ci():
    """
    Command that is run by Travis CI.
    """
    test()
    pep8()
