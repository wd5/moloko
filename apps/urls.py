from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
import datetime
now = datetime.datetime.now()

urlpatterns = patterns('',
    # Site
    
    #Afisha
    url(r'^$', 'apps.pages.views.index'),        
    url(r'^afisha/$', 'apps.events.views.events'),
    url(r'^afisha/(?P<id_event>\d+)/$', 'apps.events.views.event'),
    url(r'^afisha/all/$', 'apps.events.views.eventsAllRecent'),
    url(r'^afisha/calendar/$', 'apps.events.views.eventsCalendar',
        {
            'month':now.month,
            'year':now.year,
        }
    ),
    url(r'^afisha/calendar/(?P<year>\d{4})/(?P<month>\d{1,2})/$', 'apps.events.views.eventsCalendar'),
    url(r'^get_events/(?P<date>[^/]{10})/$', 'apps.events.views.get_events'),

    #Articles
    url(r'^articles/tag/(?P<id_tag>\d+)/$', 'apps.articles.views.by_tag'),
    url(r'^articles/(?P<divide_slug>[^/]+)/$', 'apps.articles.views.divide'),
    url(r'^articles/[^/]+/(?P<rubric_slug>[^/]+)/$', 'apps.articles.views.rubric'),
    url(r'^articles/[^/]+/[^/]+/(?P<article_slug>[^/]+)/$', 'apps.articles.views.article'),    
    url(r'^photo/$', 'apps.articles.views.by_photo'),
)