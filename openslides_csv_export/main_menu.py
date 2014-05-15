# -*- coding: utf-8 -*-

from openslides.utils.main_menu import MainMenuEntry


class CSVExportPluginMainMenuEntry(MainMenuEntry):
    """
    Main menu entry for the CSV Export Plugin for OpenSlides.
    """
    verbose_name = 'CSV Export'
    # required_permission = 'agenda.can_manage_agenda'
    permission_required = 'agenda.can_manage_agenda'  # TODO: Remove this after release of OpenSlides 1.6b2
    default_weight = 100
    pattern_name = 'csv_export_list_of_speakers'
    icon_css_class = 'icon-export'
    stylesheets = ['styles/openslides_csv_export.css']
