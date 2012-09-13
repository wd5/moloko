# -*- coding: utf-8 -*-
try:
    from config.development import *
except ImportError:
    from config.production import *

SITE_NAME = u'Молоко'

INSTALLED_APPS += (
    'apps.siteblocks',
    'apps.pages',

    #'captcha',
    'sorl.thumbnail',
    #'south',
)

MIDDLEWARE_CLASSES += (
    'apps.pages.middleware.PageFallbackMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS += (
    'apps.pages.context_processors.meta',
    'apps.siteblocks.context_processors.settings',
)