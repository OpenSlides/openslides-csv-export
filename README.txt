==================================
 CSV Export Plugin for OpenSlides
==================================

This plugin provides a csv export of the lists of speakers. It is also useful
as an example how to write plugins for OpenSlides.


Requirements
============

OpenSlides 1.4 (unreleased) (http://openslides.org)


Install
=======

1. Setup and activate a virtual environment (optional).

    $ virtualenv .venv
    $ source .venv/bin/activate

2. Install the CSV Export Plugin for OpenSlides from the Python Package Index
   or from http://openslides.org/.

    $ pip install openslides-csv-export

    or

    $ pip install http://files.openslides.org/Plugins/openslides-csv-export-1.4.tar.gz

3. Start OpenSlides once to create its settings file if it does not exist yet.

    $ openslides

4. Stop OpenSlides.

5. Edit the settings.py file. You can find it in the directory openslides
   in your user config path given in the environment variable
   $XDG_CONFIG_HOME. Default is ~/.config/openslides on GNU/Linux and
   $HOME\AppData\Local\openslides on Windows. Insert the line
   'openslides_csv_export', into the INSTALLED_PLUGINS tuple.

     INSTALLED_PLUGINS = (
         'openslides_csv_export',
     )

6. Restart OpenSlides.

    $ openslides
