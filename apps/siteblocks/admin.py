# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
from apps.siteblocks.models import SiteMenu, Settings, Banner
from apps.utils.widgets import RedactorMini
from sorl.thumbnail.admin import AdminImageMixin
from mptt.admin import MPTTModelAdmin


class SiteMenuAdmin(AdminImageMixin, MPTTModelAdmin):
    list_display = ('title', 'url', 'order', 'is_published',)
    list_display_links = ('title',)
    list_editable = ('order', 'is_published','url',)

class SettingsAdmin(admin.ModelAdmin):
    list_display = ('title',)

class BannerAdmin(AdminImageMixin, admin.ModelAdmin):
	list_display = ('id','title','url','slot','is_blank','show',)
	list_display_links = ('id','title','url',)
	list_editable = ('show','is_blank','slot',)
	list_filter = ('show','slot','is_blank',)
	search_fields = ('title',)
	radio_fields = {"slot": admin.HORIZONTAL}

admin.site.register(Settings, SettingsAdmin)
admin.site.register(SiteMenu, SiteMenuAdmin)
admin.site.register(Banner, BannerAdmin)
  