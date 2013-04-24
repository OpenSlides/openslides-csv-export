#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
URL patterns.
"""

from django.conf.urls import url, patterns

from .views import CSVExportView


urlpatterns = patterns(
    '',
    url(r'^lists_of_speakers/$',
        CSVExportView.as_view(),
        name='csv_export_list_of_speakers'))
