==================================
 CSV Export Plugin for OpenSlides
==================================

Version 1.0b1 (2013-06-04)

This plugin provides a csv export of the lists of speakers. It is also useful
as an example how to write plugins for OpenSlides.


Requirements
============

OpenSlides 1.4b2 (http://openslides.org/)


Install
=======

This is only an example instruction for install on GNU/Linux. CSV Export
Plugin for OpenSlides can also be installed as any other python package,
e. g. on Windows.

1. Change to a new directory.

    $ mkdir OpenSlides

    $ cd OpenSlides

2. Setup and activate a virtual environment and install OpenSlides in it.

    $ virtualenv .venv

    $ source .venv/bin/activate

    $ pip install http://files.openslides.org/Beta/openslides-1.4b2.tar.gz

3. Install the CSV Export Plugin for OpenSlides from http://openslides.org/.

    $ pip install http://files.openslides.org/plugins/openslides-csv-export/openslides-csv-export-1.0b1.tar.gz

4. Start OpenSlides once to create its settings file if it does not exist yet.

    $ openslides

5. Stop OpenSlides.

6. Edit the settings.py file. You can find it in the directory openslides
   in your user config path given in the environment variable
   $XDG_CONFIG_HOME. Default is ``~/.config/openslides`` on GNU/Linux (and
   ``$HOME\AppData\Local\openslides`` on Windows). Insert the line
   'openslides_csv_export' into the INSTALLED_PLUGINS tuple.

     INSTALLED_PLUGINS = (
         'openslides_csv_export',
     )

7. Restart OpenSlides.

    $ openslides
