import datetime
import time

from django.contrib.auth import get_user_model
from openslides.agenda.models import Speaker
from openslides.core.models import CustomSlide
from openslides.utils.test import TestCase


class CSVExportView(TestCase):
    """
    Tests the export view and its output, the csv file.
    """
    def setUp(self):
        self.admin = get_user_model().objects.get(username='admin')
        self.client.login(username='admin', password='admin')

    def test_get_manager(self):
        response = self.client.get('/csv_export_lists_of_speakers/')
        self.assertContains(response, 'Item,Person,Begin Time,End Time', status_code=200)

    def test_get_normal_user(self):
        self.client.logout()
        response = self.client.get('/csv_export_lists_of_speakers/')
        self.assertEqual(response.status_code, 403)

    def test_csv_content(self):
        customslide = CustomSlide.objects.create(title='Iangohse5pae7eineeca')
        speaker1 = Speaker.objects.add(self.admin, customslide.agenda_item)
        response = self.client.get('/csv_export_lists_of_speakers/')
        self.assertContains(response, 'Iangohse5pae7eineeca,{},'.format(str(self.admin)), status_code=200)
        speaker1.begin_speech()
        response = self.client.get('/csv_export_lists_of_speakers/')
        text = 'Iangohse5pae7eineeca,{},{}'.format(
            str(self.admin),
            datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S'))
        self.assertContains(response, text, status_code=200)
        time.sleep(1)
        speaker1.end_speech()
        response = self.client.get('/csv_export_lists_of_speakers/')
        text = ','.join((text, datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')))
        self.assertContains(response, text, status_code=200)
