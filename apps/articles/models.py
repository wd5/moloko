# -*- coding: utf-8 -*-
from django.db import models
import os,datetime
from sorl.thumbnail import ImageField
from pytils.translit import translify
from apps.utils.managers import VisibleObjects
from django.utils.translation import ugettext_lazy as _

from apps.events.models import Event

class Divide(models.Model):
	title = models.CharField(
		u'название раздела',
		max_length = 150,
	)
	order = models.IntegerField(
		u'порядок сортировки',
		help_text=u'Чем больше число, тем выше располагается элемент',
		default = 10
	)
	slug = models.SlugField(
		u'Алиас',
		help_text=u'Уникальное имя на латинице',
		unique=True,
	)

	# свой manager для отображения show = True
	show = models.BooleanField(
		verbose_name=u'Отображать',
		 default=True
	)
	objects = models.Manager() # The default manager.
	items = VisibleObjects() # The visible objects manager.
	# 

	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ['-order']
		verbose_name = _(u'divide') 
		verbose_name_plural = _(u'divides')
		
	def get_absolute_url(self):
		return u'/articles/%s/' % self.slug

	def get_rubrics(self):
		return self.rubric_set.all()

	def get_articles(self):
		rubrics = self.get_rubrics()
		articles = Article.items.select_related().filter(rubric__in=rubrics)
		return articles

class Rubric(models.Model):
	divide =  models.ForeignKey(
		Divide,
		verbose_name = u'раздел'
	)
	title = models.CharField(
		u'название рубрики',
		max_length = 150,
	)
	order = models.IntegerField(
		u'порядок сортировки',
		help_text=u'Чем больше число, тем выше располагается элемент',
		default = 10
	)
	slug = models.SlugField(
		u'Алиас',
		help_text=u'Уникальное имя на латинице'
	)
	# свой manager для отображения show = True
	show = models.BooleanField(
		verbose_name=u'Отображать',
		 default=True
	)
	objects = models.Manager() # The default manager.
	items = VisibleObjects() # The visible objects manager.
	# 
	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ['-order']
		verbose_name = _(u'rubric')
		verbose_name_plural = _(u'rubris')

	def get_absolute_url(self):
		return u'%s%s/' % (self.divide.get_absolute_url(),self.slug)

	def get_articles(self):
		return self.article_set.filter(show=True)

class Tag(models.Model):
	title = models.CharField(
		u'название',
		max_length = 150,
	)

	class Meta:
		verbose_name = _(u'tag')
		verbose_name_plural = _(u'tags')

	def __unicode__(self):
		return self.title

	def get_articles(self):
		return self.article_set.all()

class Spec_project(models.Model):
	title = models.CharField(
		u'название спец.проекта',
		max_length = 150,
	)
	order = models.IntegerField(
		u'порядок сортировки',
		help_text=u'Чем больше число, тем выше располагается элемент',
		default = 10
	)

	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ['-order']
		verbose_name = _(u'spec.project')
		verbose_name_plural = _(u'spec.projects')

	def get_articles(self):
		return self.article_set.all()

def file_path_Article(instance, filename):
	return os.path.join('images','articles', translify(filename).replace(' ', '_') )

class Author(models.Model):
	fullname = models.CharField(
		u'ФИО автора',
		max_length = 150,
	)
	
	def __unicode__(self):
		return self.fullname

	class Meta:		
		verbose_name = _(u'author')
		verbose_name_plural = _(u'authors')

	def get_articles(self):
		return self.article_set.all()

class Article(models.Model):
	author = models.ForeignKey(
		Author,
		verbose_name = u'автор'
	)	
	spec_project =  models.ForeignKey(
		Spec_project,
		verbose_name = u'спец.проект',
		blank = True,
		null = True,
	)
	tag = models.ManyToManyField(
		Tag,
		verbose_name = u'тэг',
		blank = True,
		null = True,
	)
	eventURL = models.ForeignKey(
		Event,
		verbose_name = u'ссылка на событие',
		blank = True,
		null = True,
	)	
	rubric =  models.ForeignKey(
		Rubric,
		verbose_name = u'рубрика'
	)
	title = models.CharField(
		u'название статьи',
		max_length = 150,
	)
	date_create = models.DateTimeField(
		u'дата публикации',
		default=datetime.datetime.now
	)	
	short_text = models.TextField(
		u'краткое описание',
		blank=True
	)
	text = models.TextField(
		u'текст статьи'
	)
	image = ImageField(
		upload_to=file_path_Article,
		verbose_name = u'картинка',
		blank = True,
		null = True,
	)
	is_on_main = models.BooleanField(
		u'отображать на главной',
		default = False
	)
	slug = models.SlugField(
		u'Алиас',
		help_text=u'Уникальное имя на латинице',
		unique=True
	)
	# свой manager для отображения show = True
	show = models.BooleanField(
		verbose_name=u'Отображать',
		 default=True
	)
	objects = models.Manager() # The default manager.
	items = VisibleObjects() # The visible objects manager.
	# 

	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ['-date_create']
		verbose_name = _(u'article_item')
		verbose_name_plural = _(u'article_items')

	def get_albums(self):
		return self.photoalbum_set.all()

	def get_absolute_url(self):
		return u'%s%s/' % (self.rubric.get_absolute_url(),self.slug)

class PhotoAlbum(models.Model):
	article = models.ForeignKey(
		Article,
		verbose_name = u'статья',
		blank = True,
		null = True
	)
	author = models.CharField(
		u'автор',
		max_length = 150,
		blank=False,
	)
	date_create = models.DateTimeField(
		u'дата создания',
		default=datetime.datetime.now
	)
	# свой manager для отображения show = True
	show = models.BooleanField(
		verbose_name=u'Отображать',
		 default=True
	)
	objects = models.Manager() # The default manager.
	items = VisibleObjects() # The visible objects manager.
	# 

	def __unicode__(self):
		#if self.article:
		#	article = self.article
		#else:
		#	article = u"Не прикреплен"		
		#return "%s - %s (%s)" % (article, self.author, self.date_create)
		return "%s - %s" % (self.author, self.date_create)

	class Meta:
		ordering = ['-date_create']
		verbose_name = _(u'photoalbum')
		verbose_name_plural = _(u'photoalbums')
	
	def get_photos(self):
		return self.photo_album.filter(show=True)

def file_path_Photo(instance, filename):
	return os.path.join('images','photos', translify(filename).replace(' ', '_') )

class Photo(models.Model):
	image = ImageField(
		upload_to=file_path_Photo,
		verbose_name = u'фотография',
	)
	title = models.CharField(
		u'название',
		max_length = 150,
		blank=True,
		null=True,
	)
	photoAlbum =  models.ForeignKey(
		PhotoAlbum,
		verbose_name = u'фотоальбом',
		related_name = u'photo_album'
	)
	order = models.IntegerField(
		u'порядок сортировки',
		help_text = u'Чем больше число, тем выше располагается элемент',
		default = 10,
	)	
	show = models.BooleanField(
		verbose_name=u'Отображать',
		 default=True
	)

	def __unicode__(self):		
		return u'%s' % self.title

	class Meta:
		ordering = ['-order']
		verbose_name = _(u'photo')
		verbose_name_plural = _(u'photos')

	
    