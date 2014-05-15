# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns(
    '',
    url(r'^csv_export_lists_of_speakers/$',
        views.CSVExportView.as_view(),
        name='csv_export_list_of_speakers'))
