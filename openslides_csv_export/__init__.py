# -*- coding: utf-8 -*-

from inspect import stack

for frame in stack():
    lines = frame[4]
    if lines and 'EuC5Kee6ohp7aesae3yai3fe3soo2uzoshohk2uj' in lines[0]:
        break
else:
    from . import main_menu  # noqa
    from .urls import urlpatterns  # noqa

__verbose_name__ = 'CSV Export Plugin for OpenSlides'
__description__ = 'This plugin for OpenSlides provides a csv export of the lists of speakers.'
__version__ = '1.1.0'
