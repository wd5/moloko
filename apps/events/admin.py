# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
from apps.events.models import Event
from apps.utils.widgets import Redactor
from sorl.thumbnail.admin import AdminImageMixin

class EventAdminForm(forms.ModelForm):
	description = forms.CharField(widget=Redactor(attrs={'cols': 200, 'rows': 30}))
	description.label=u'описание события'
	
	class Meta:
		model = Event

class EventAdmin(AdminImageMixin,admin.ModelAdmin):
	list_display = ('id','title','place','date_create','show')
	list_display_links = ('id','title','place',)
	list_editable = ('show',)
	list_filter = ('show','date_create','place',)
	search_fields = ('title','place','description',)
	form = EventAdminForm

admin.site.register(Event, EventAdmin)