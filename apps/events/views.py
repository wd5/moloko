# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect,Http404,HttpResponseBadRequest,HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic.simple import direct_to_template
from apps.events.models import Event
import datetime
import calendar
from calendar import monthrange
from django.shortcuts import render_to_response

def events(request):
	now = datetime.datetime.now()
	allEvents = Event.items.all()
	eventsSoon = allEvents.filter(date_create__gte=now).order_by('date_create')[:12]
	month = now.month
	eventsRecent = allEvents.filter(date_create__lt=now).order_by('-date_create')[:12]
	return direct_to_template(
		request,
		'events/events.html',
		{
			'eventsSoon':eventsSoon,
			'eventsRecent':eventsRecent,
		}
	)

def eventsAllRecent(request):
	now = datetime.datetime.now()	
	RecentEvents = Event.items.filter(date_create__lt=now)
	return direct_to_template(
		request,
		'events/events.html',
		{
			'allRecentEvents':RecentEvents,
		}
	)

def event(request,id_event):
	try:
		event = Event.items.get(id=id_event)
	except Event.DoesNotExist:
		#raise Http404 
		return HttpResponseRedirect('/')
	return direct_to_template(
		request,
		'events/events.html',
		{
			'event':event,
		}
	)

def eventsCalendar(request,month,year):

	month = int(month)
	year = int(year)	
	dateNow = datetime.date(year,month,1)

	class monthDateCount():
		date = datetime.date(12,12,12)
		countEvents = 0
		def __unicode__(self):
			return u'%s - %s' % (self.date,self.countEvents)

	daysInMonth = monthrange(year, month)	
	start = dateNow.weekday()
	monthDateArray=range(daysInMonth[1]+start)
	for i in range(start,daysInMonth[1]+start):		
		obj=monthDateCount()
		day = i+1-start	
		obj.date = datetime.date(year, month, day)
		obj.countEvents = Event.items.filter(date_create__year=obj.date.year,date_create__month=obj.date.month,date_create__day=obj.date.day).count()
 		monthDateArray[i] = obj

	if month == 12:		
		nextDate = datetime.date(year+1, 1, 1)
	else:		
		nextDate = datetime.date(year, month+1, 1)	
	if month == 1:		
		prevDate = datetime.date(year-1, 12, 1)
	else:		
		prevDate = datetime.date(year, month - 1, 1)

	return direct_to_template(
		request,
		'events/eventsCalendar.html',
		{
			'datetime':dateNow,
			'nextDate':nextDate,
			'prevDate':prevDate,
			'monthDateArray':monthDateArray,	
			'start':start,
		}
	)

def get_events(request,date):
	date=date.split('.')
	now = datetime.datetime.now()	
	try:
		day=date[0]
		day = int(day)
	except (IndexError, ValueError):
		return HttpResponseBadRequest()
	try:
		month=date[1]
		month = int(month)		
	except (IndexError, ValueError):	
		return HttpResponseBadRequest()
	try:
		year=date[2]		
		year = int(year)				
	except (IndexError, ValueError):	
		return HttpResponseBadRequest()

	nowDay = now.day
	nowMonth = now.month
	nowYear = now.year
	#return HttpResponse(u'%s'%day)
	if month not in range(1,13):
		return HttpResponseBadRequest()
	if day not in range(1,32):
		return HttpResponseBadRequest()
	if year not in range(nowYear-20,nowYear+20):
		return HttpResponseBadRequest()		
	date = datetime.date(year,month,day)
	events = Event.items.filter(date_create__year=date.year,date_create__month=date.month,date_create__day=date.day)
	return render_to_response(
		'events/eventsFancybox.html',
		{
			'events':events,
			'date':date,
		}
	)