# -*- coding: utf-8 -*-
from django.db import models
import os,datetime
from sorl.thumbnail import ImageField
from pytils.translit import translify
from django.utils.translation import ugettext_lazy as _
from apps.utils.managers import VisibleObjects

def file_path_Event(instance, filename):
	return os.path.join('images','events', translify(filename).replace(' ', '_') )

class Event(models.Model):
	title = models.CharField(
		u'название события',
		max_length = 150,
	)	
	date_create = models.DateTimeField(
		u'дата проведения',
		default=datetime.datetime.now
	)
	place = models.CharField(
		u'место проведения',
		max_length = 255,
	)
	image = ImageField(
		upload_to = file_path_Event,
		verbose_name = u'картинка',
	)
	description = models.TextField( #redactor
		u'описание события'
	)
	# свой manager для отображения show = True
	show = models.BooleanField(
		verbose_name=u'Отображать',
		 default=True
	)
	objects = models.Manager() # The default manager.
	items = VisibleObjects() # The visible objects manager.
	# 
	
	class Meta:
		ordering = ['-date_create']
		verbose_name = _(u'eventItem')
		verbose_name_plural = _(u'eventItems')

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return u'/afisha/%s/' %  self.id

	def get_articles(self):
		return self.article_set.all()
