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

    $ pip install openslides-csv-export==1.1.0

Start OpenSlides once to create its settings file if it does not exist yet::

    $ openslides

Stop OpenSlides::

    CTRL + C

Edit the file ``settings.py``. You can find it in the directory
``openslides`` in your user config path given in the environment variable
``$XDG_CONFIG_HOME``. Default is ``~/.config/openslides/`` on GNU/Linux and
``$HOME\AppData\Local\openslides\`` on Windows. Insert the line
``'openslides_csv_export',`` into the INSTALLED_PLUGINS tuple::

    # Add OpenSlides plugins to this tuple
    INSTALLED_PLUGINS = (
        'openslides_csv_export',
    )

Restart OpenSlides::

    $ openslides


License and authors
===================

This plugin is released under the MIT License, see LICENSE file. The
authors of this plugin are mentioned in the AUTHORS file.


Changelog
=========

Version 1.1.0 (unreleased)
--------------------------
* Updated to new plugin api of OpenSlides 1.6.


Version 1.0.2 (2013-11-26)
--------------------------
* Updated to OpenSlides 1.5.x.


Version 1.0.1 (2013-07-30)
--------------------------
* Updated to OpenSlides 1.4.1.


Version 1.0 (2013-07-11)
------------------------
* First release of this plugin.
