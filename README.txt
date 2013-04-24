==================================
 CSV Export Plugin for OpenSlides
==================================

This Plugin provides an csv export of the lists of speakers.


Requirements
============

OpenSlides 1.4 (http://openslides.org)


Install
=======

1. Install OpenSlides into a virtual environment, see INSTALL.txt of OpenSlides.

2. Activate this virtual environment

    $ source .venv/bin/activate

3. Install the CSV Export Plugin for OpenSlides from the Python Package Index.

    $ pip install openslides-csv-export

4. Start OpenSlides once to create its settings file.

    $ python start.py

    or just

    $ openslides

5. Edit the settings file. You can find in the directory openslides in your
   user config path given in the environment variable $XDG_CONFIG_HOME.
   Default is ~/.config/openslides on GNU/Linux and $HOME\AppData\Local\openslides
   on Windows. Insert the line 'openslides_csv_export,' into the INSTALLED_PLUGINS
   tuple.

6. Restart openslides.
