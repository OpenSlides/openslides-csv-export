#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Setup script for the csv-export plugin.
"""

from setuptools import setup
from setuptools import find_packages


with open('README.txt') as file:
    long_description = file.read()

setup(
    name='csv-export',
    long_description=long_description,
    version="0.1",
    author='OpenSlides-Team',
    author_email='support@openslides.org',
    license='GPL2+',
    packages=find_packages(),
    include_package_data=True,
    setup_requires=[
        'versiontools >= 1.6',
    ],
    install_requires=[
        'openslides',
    ],
)
