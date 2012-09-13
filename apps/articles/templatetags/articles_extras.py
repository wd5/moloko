# -*- coding: utf-8 -*-
from apps.articles.models import Divide,Rubric,Article,PhotoAlbum
from apps.events.models import Event
import datetime

from django import template

register = template.Library()
now = datetime.datetime.now()

@register.inclusion_tag("articles/r_block.html")
def r_block(type,divide_slug):
	bottom_link = ''
	bottom_link_url = ''
	if type == 'events':
		result = Event.items.all().filter(date_create__gte=now).order_by('date_create')[:4]
		block_name = 'Скоро'
		bottom_link = 'все события'
		bottom_link_url = '/afisha/'
	elif type == 'photos':
		block_name = 'Фото'
		bottom_link = 'все фоторепортажи'
		bottom_link_url = '/photo/'
		article_id_list = PhotoAlbum.items.filter(article__isnull=False).values_list('article', flat=True)
		result = Article.items.filter(pk__in=article_id_list).exclude(image='').order_by('-date_create')[:10]
	elif type == 'articles':
		result = Article.items.all()
		block_name = 'Свежее'
		result = Article.items.all()[:7]
	elif type == 'rubrics':
		divide = Divide.items.get(slug=divide_slug)
		result = divide.get_rubrics()
		block_name = 'Рубрики'
	else:
		result = False

	return {'items':result,'block_name':block_name,'bottom_link':bottom_link,'bottom_link_url':bottom_link_url,'type':type}