# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect,Http404
from django.shortcuts import get_object_or_404
from django.views.generic.simple import direct_to_template
from apps.articles.models import Divide,Rubric,Article,Tag,PhotoAlbum

def divide(request,divide_slug):
	try:
		divide = Divide.items.get(slug=divide_slug)
	except Divide.DoesNotExist:
		#raise Http404 
		return HttpResponseRedirect('/')	
	articles = divide.get_articles()[:7]
	return direct_to_template(
		request,
		'articles/articles_by.html',
		{
			'articles':articles,
			'divideTitle':divide.title,
			'divide_slug':divide.slug,
		}
	)

def rubric(request,rubric_slug):
	try:
		rubric = Rubric.items.get(slug=rubric_slug)
	except Rubric.DoesNotExist:
		#raise Http404 
		return HttpResponseRedirect('/')	
	articles = rubric.get_articles()[:7]
	return direct_to_template(
		request,
		'articles/articles_by.html',
		{
			'articles':articles,
			'divideTitle':rubric.divide.title,
			'divide_slug':rubric.divide.slug,
		}
	)

def article(request,article_slug):
	try:
		article = Article.items.get(slug=article_slug)
	except Article.DoesNotExist:
		#raise Http404 
		return HttpResponseRedirect('/')
	return direct_to_template(
		request,
		'articles/articles_by.html',
		{
			'article':article,
			'divideTitle':article.rubric.divide.title,
			'divide_slug':article.rubric.divide.slug,
		}
	)

def by_tag(request,id_tag):
	try:
		tag = Tag.objects.get(id=id_tag)
	except Tag.DoesNotExist:
		#raise Http404 
		return HttpResponseRedirect('/')	
	articles = tag.get_articles()[:7]
	return direct_to_template(
		request,
		'articles/articles_by.html',
		{
			'articles':articles,
			'tagTitle':tag.title,			
		}
	)

def by_photo(request):
	article_id_list = PhotoAlbum.items.filter(article__isnull=False).values_list('article', flat=True)
	articles = Article.items.filter(pk__in=article_id_list).exclude(image='').order_by('-date_create')[:9]	
	return direct_to_template(
		request,
		'articles/articles_by.html',
		{
			'articles':articles,
			'photo':'Фото',			
		}
	)