#!/usr/bin/env python
# -*- coding: utf-8 -*-

NAME = 'openslides-csv-export'
VERSION = '1.4b1-dev'
DESCRIPTION = 'CSV Export Plugin for OpenSlides'


def get_name():
    """
    Function for OpenSlides' version page.
    """
    return '%s (%s)' % (DESCRIPTION, NAME)
