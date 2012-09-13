from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings

from apps.urls import urlpatterns as appsUrl

admin.autodiscover()

urlpatterns = patterns('',

    # Admin
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin_tools/', include('admin_tools.urls')),

     #Redactor
    (r'^upload_img/$', 'views.upload_img'),
    (r'^upload_file/$', 'views.upload_file'),

    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.ADMIN_MEDIA_ROOT}),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    
)

urlpatterns += appsUrl