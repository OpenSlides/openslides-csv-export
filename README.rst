==================================
 CSV Export Plugin for OpenSlides
==================================

Overview
========

This plugin for OpenSlides provides a csv export of the lists of speakers.
It is also useful as an example how to write plugins for OpenSlides.


Requirements
============

OpenSlides 1.6.x (http://openslides.org/)


Install
=======

This is only an example instruction for install CSV Export Plugin for
OpenSlides on GNU/Linux. It can also be installed as any other python
package and on other platforms, e. g. on Windows.

Change to a new directory::

    $ cd

    $ mkdir OpenSlides

    $ cd OpenSlides

Setup and activate a virtual environment and install OpenSlides in it::

    $ virtualenv .virtualenv

    $ source .virtualenv/bin/activate

    $ pip install "openslides>=1.6,<1.7"  # or http://files.openslides.org/releases/1.6/openslides-1.6.tar.gz

Install CSV Export Plugin for OpenSlides from the Python Package Index (PyPI)::

    $ pip install openslides-csv-export

Start OpenSlides::

    $ openslides


License and authors
===================

This plugin is Free/Libre Open Source Software and distributed under the
MIT License, see LICENSE file. The authors are mentioned in the AUTHORS file.


Changelog
=========

Version 1.1.0 (2014-06-02)
--------------------------
* Updated to new plugin api and to other api changes of OpenSlides 1.6.
* Fixed bug when using related agenda items.


Version 1.0.2 (2013-11-26)
--------------------------
* Updated to OpenSlides 1.5.x.


Version 1.0.1 (2013-07-30)
--------------------------
* Updated to OpenSlides 1.4.1.


Version 1.0 (2013-07-11)
------------------------
* First release of this plugin.
