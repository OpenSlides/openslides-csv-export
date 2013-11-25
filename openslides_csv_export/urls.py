# -*- coding: utf-8 -*-

from django.conf.urls import url, patterns

from . import views


urlpatterns = patterns(
    '',
    url(r'^lists_of_speakers/$',
        views.CSVExportView.as_view(),
        name='csv_export_list_of_speakers'))
