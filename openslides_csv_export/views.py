#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Views to export data as csv files.
"""

import csv
import StringIO

from django.http import HttpResponse

from openslides.utils.views import View, PermissionMixin
from openslides.agenda.models import Speaker


class CSVExportView(PermissionMixin, View):
    """
    View to export the lists of speakers of all agenda items as csv.
    """
    permission_required = 'agenda.can_manage_agenda'

    def get(self, request, *args, **kwargs):
        response = HttpResponse()
        response['Content-Disposition'] = 'attachment; filename=list_of_speakers.csv;'
        csv_writer = csv.writer(response)
        csv_writer.writerow(['Item', 'Person', 'Begin Time', 'End Time'])
        for speaker in Speaker.objects.all().order_by('item', 'weight', 'begin_time'):
            try:
                begin_time = speaker.begin_time.strftime('%d.%m.%Y %H:%M:%S')
            except AttributeError:
                begin_time = None
            try:
                end_time = speaker.end_time.strftime('%d.%m.%Y %H:%M:%S')
            except AttributeError:
                end_time = None
            csv_writer.writerow([
                speaker.item.title.encode('utf8'), unicode(speaker.person).encode('utf8'), begin_time, end_time])
        return response
