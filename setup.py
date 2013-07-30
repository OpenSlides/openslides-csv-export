#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Setup script for CSV Export Plugin for OpenSlides.
"""

from setuptools import setup, find_packages

from openslides_csv_export import NAME, VERSION, DESCRIPTION


with open('README.rst') as readme:
    long_description = readme.read()


with open('requirements_production.txt') as requirements_production:
    install_requires = requirements_production.readlines()


setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    author='OpenSlides-Team, see AUTHORS',
    author_email='support@openslides.org',
    url='http://openslides.org',
    keywords='OpenSlides',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2'],
    license='MIT',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    install_requires=install_requires)
