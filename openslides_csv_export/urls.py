from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^csv_export_lists_of_speakers/$',
        views.CSVExportView.as_view(),
        name='csv_export_list_of_speakers'),
]
