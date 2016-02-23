from django.apps import AppConfig

from . import __description__, __verbose_name__, __version__


class CSVExportAppConfig(AppConfig):
    name = 'openslides_csv_export'
    verbose_name = __verbose_name__
    description = __description__
    version = __version__
    angular_site_module = True
    angular_projector_module = False
    js_files = [
        'js/openslides_csv_export/base.js',
        'js/openslides_csv_export/site.js']

    def ready(self):
        # Add urlpatters to application configuration.
        from .urls import urlpatterns

        self.urlpatterns = urlpatterns
