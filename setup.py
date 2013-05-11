#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Setup script for the CSV Export Plugin for OpenSlides.
"""

from setuptools import setup, find_packages

from openslides_csv_export import VERSION


with open('README.txt') as readme:
    long_description = readme.read()


setup(
    name='openslides-csv-export',
    version=VERSION,
    description='CSV Export Plugin for OpenSlides',
    long_description=long_description,
    author='OpenSlides-Team, see AUTHORS',  # TODO: Check this.
    author_email='support@openslides.org',  # TODO: Check this.
    url='http://openslides.org',
    packages=find_packages(exclude=['tests']),
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2'],
    license='MIT',
    install_requires='openslides== 1.4')


