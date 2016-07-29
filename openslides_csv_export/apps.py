from django.apps import AppConfig

from . import __description__, __verbose_name__, __version__


class CSVExportAppConfig(AppConfig):
    name = 'openslides_csv_export'
    verbose_name = __verbose_name__
    description = __description__
    version = __version__
    angular_site_module = True
    angular_projector_module = False  # TODO
    js_files = [
        'static/js/openslides_csv_export/base.js',
        'static/js/openslides_csv_export/site.js',
    ]

    def ready(self):
        # Add plugin urlpatters to application configuration so OpenSlides
        # can find it.
        from .urls import urlpatterns

        self.urlpatterns = urlpatterns
