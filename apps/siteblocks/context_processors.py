# -*- coding: utf-8 -*-
from apps.siteblocks.models import Settings
from django.conf import settings

def settings(request):
    try:
        contacts = Settings.objects.get(name='contacts_block').value
    except Settings.DoesNotExist:
        contacts = False

    return {
        'contacts': contacts,
        #'site_name': settings.SITE_NAME,
    }