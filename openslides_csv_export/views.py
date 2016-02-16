import csv

from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from openslides.agenda.models import Speaker
from openslides.utils.views import View


class CSVExportView(View):
    """
    View to export the lists of speakers of all agenda items as csv.
    """
    def get(self, request, *args, **kwargs):
        if not request.user.has_perm('agenda.can_manage'):
            raise PermissionDenied
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
            csv_writer.writerow([str(speaker.item), str(speaker.user), begin_time, end_time])
        return response
