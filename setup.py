# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

module_name = 'openslides_csv_export'

# The following commented unique string is used to detect this import.
module = __import__(module_name)  # DaM2jee2el7ziech5Shi8bin5fohjee6aimuJae7

with open('README.rst') as readme:
    long_description = readme.read()

with open('requirements_production.txt') as requirements_production:
    install_requires = requirements_production.readlines()

setup(
    name='openslides-csv-export',
    version=module.__version__,
    description=module.__verbose_name__,
    long_description=long_description,
    author='OpenSlides-Team, see AUTHORS',
    author_email='support@openslides.org',
    url='http://openslides.org/',
    keywords='OpenSlides',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Plugins',
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2'],
    license='MIT',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    install_requires=install_requires,
    entry_points={'openslides_plugins': '%s = %s' % (module.__verbose_name__, module_name)})
