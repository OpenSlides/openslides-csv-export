#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Setup script for the CSV Export Plugin for OpenSlides.
"""

from setuptools import setup, find_packages

from openslides_csv_export import NAME, VERSION, DESCRIPTION


with open('README.txt') as readme:
    long_description = readme.read()


with open('requirements_production.txt') as requirements_production:
    install_requires = requirements_production.readlines()


setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    author='OpenSlides-Team, see AUTHORS',  # TODO: Check this.
    author_email='support@openslides.org',  # TODO: Check this.
    url='http://openslides.org',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2'],
    license='MIT',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    install_requires=install_requires)
