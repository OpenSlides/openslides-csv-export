#!/usr/bin/env python
# -*- coding: utf-8 -*-

from inspect import stack

lines = stack()[-1][4]

if not (lines and 'DaM2jee2el7ziech5Shi8bin5fohjee6aimuJae7' in lines[0]):
    from .urls import urlpatterns  # noqa

__description__ = 'This plugin for OpenSlides provides a csv export of the lists of speakers.'
__verbose_name__ = 'CSV Export Plugin for OpenSlides'
__version__ = '1.1.0-dev'
