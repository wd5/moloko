# -*- coding: utf-8 -*-
import os

PROJECT_NAME = 'three_dx'

ROOT_PATH = os.path.dirname(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

TIME_ZONE = 'Europe/Moscow'
LANGUAGE_CODE = 'ru-RU'

PYMORPHY_DICTS = {
    'ru': { 'dir': '/usr/share/pymorphy/ru' },
}

SITE_ID = 1

USE_I18N = True
USE_L10N = True

MEDIA_ROOT = ROOT_PATH + '/static/'
MEDIA_URL = '/static/'

# URL prefix for static files.
STATIC_ROOT = ROOT_PATH + '/static/'
STATIC_URL = '/static/'

ADMIN_MEDIA_PREFIX = '/media/'
ADMIN_MEDIA_ROOT = ROOT_PATH + '/media/'

SECRET_KEY = 'n56Uidrtu}ig%#hgjh$pbdvwlju7b'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

'''
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
)
'''

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.csrf.CsrfResponseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'pagination.middleware.PaginationMiddleware',    
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    #'django.contrib.messages.context_processors.messages',
    #'django.core.context_processors.media',
    #'django.core.context_processors.static',
    'apps.utils.context_processors.custom_proc',
)

INSTALLED_APPS = (
    #'admintools_bootstrap',
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    #'django.contrib.staticfiles',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'mptt',
    'apps.pages',
    'apps.siteblocks',
    'apps.articles',
    'apps.events',
    'sorl.thumbnail',
    'pagination',
    'pymorphy',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    os.path.join(ROOT_PATH, 'templates')
)

MPTT_ADMIN_LEVEL_INDENT = 20
CAPTCHA_NOISE_FUNCTIONS = ()

ADMIN_TOOLS_INDEX_DASHBOARD = 'dashboard.CustomIndexDashboard'
ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'dashboard.CustomAppIndexDashboard'
ADMIN_TOOLS_MENU = 'menu.CustomMenu'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
