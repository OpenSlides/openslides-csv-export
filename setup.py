#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Setup script for the CSV Export Plugin for OpenSlides.
"""

from setuptools import setup
from setuptools import find_packages

from openslides_csv_export import VERSION


with open('README.txt') as readme:
    long_description = readme.read()


setup(
    name='openslides-csv-export',
    version=VERSION,
    author='OpenSlides-Team, see AUTHORS',  # TODO: Check this.
    author_email='support@openslides.org',  # TODO: Check this.
    url='http://openslides.org',
    description='CSV Export Plugin for OpenSlides',
    long_description=long_description,
    #classifiers=[],  # TODO: Complete this.
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    setup_requires=['versiontools >= 1.6'],
    install_requires=['openslides'])
