#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url, patterns
from .views import CSVExportView


urlpatterns = patterns('',
    url(r'^list_of_speakers/$',
        CSVExportView.as_view(),
        name='csvexport_list_of_speakers',
    ),
)
