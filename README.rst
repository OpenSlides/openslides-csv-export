==================================
 CSV Export Plugin for OpenSlides
==================================

Version 1.0.1 (2013-07-30)

Overview
========

This plugin for OpenSlides provides a csv export of the lists of speakers.
It is also useful as an example how to write plugins for OpenSlides.


Requirements
============

OpenSlides 1.4.1 (http://openslides.org/)


Install
=======

This is only an example instruction for install CSV Export Plugin for
OpenSlides on GNU/Linux. It can also be installed as any other python
package and on other platforms, e. g. on Windows.

Change to a new directory::

    $ mkdir OpenSlides

    $ cd OpenSlides

Setup and activate a virtual environment and install OpenSlides in it::

    $ virtualenv .venv

    $ source .venv/bin/activate

    $ pip install openslides==1.4.1  # or http://files.openslides.org/openslides-1.4.1.tar.gz

Install CSV Export Plugin for OpenSlides from http://openslides.org/::

    $ pip install http://files.openslides.org/plugins/openslides-csv-export/openslides-csv-export-1.0.1.tar.gz

Instead of the last step you can also just use the Python Package Index (PyPI)::

    $ pip install openslides-csv-export==1.0.1

Start OpenSlides once to create its settings file if it does not exist yet::

    $ openslides

Stop OpenSlides::

    CTRL + C

Edit the ``settings.py`` file. You can find it in the directory
``openslides`` in your user config path given in the environment variable
``$XDG_CONFIG_HOME``. Default is ``~/.config/openslides/`` on GNU/Linux and
``$HOME\AppData\Local\openslides\`` on Windows. Insert the line
``openslides_csv_export,`` into the INSTALLED_PLUGINS tuple::

    # Add OpenSlides plugins to this list
    INSTALLED_PLUGINS = (
        'openslides_csv_export',
    )

Restart OpenSlides::

    $ openslides


Changelog
=========

Version 1.0.1 (2013-07-30)
--------------------------
* Update to OpenSlides 1.4.1


Version 1.0 (2013-07-11)
------------------------
* First release of this plugin.
