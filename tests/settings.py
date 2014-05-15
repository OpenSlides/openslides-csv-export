# -*- coding: utf-8 -*-
#
# Settings file for tests only
#

import os
from openslides.global_settings import *  # noqa

DEBUG = True
TEMPLATE_DEBUG = DEBUG

SECRET_KEY = 'secret'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': ''}}

INSTALLED_PLUGINS += (
    'openslides_csv_export',)

INSTALLED_APPS += INSTALLED_PLUGINS

TIME_ZONE = 'Europe/Berlin'

MEDIA_ROOT = ''

# Use RAM storage
HAYSTACK_CONNECTIONS['default']['STORAGE'] = 'ram'

TEMPLATE_DIRS = (
    filesystem2unicode(os.path.join(SITE_ROOT, 'templates')),)

STATICFILES_DIRS = (
    filesystem2unicode(os.path.join(SITE_ROOT, 'static')),)

# Use a faster passwort hasher
PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',)
