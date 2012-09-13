# -*- coding: utf-8 -*-
from apps.pages.models import MetaData
from django.contrib.sites.models import Site
from django.contrib.auth.forms import AuthenticationForm

def custom_proc(request):
    try:
        meta = MetaData.objects.get(url = request.path)
    except MetaData.DoesNotExist:
        try:
            meta = MetaData.objects.get(url = u'/')
        except MetaData.DoesNotExist:
            meta = False
    try:
        site = Site.objects.get_current()
    except Site.DoesNotExist:
        site = False

    current_url = request.path

    return {
        'meta': meta,
        'current_url':current_url,
        'site_name':site.name,
    }