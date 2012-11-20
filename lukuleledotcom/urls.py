from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
# from django.contrib.admin.views import main

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('lukuleledotcom.views',
	url(r'^admin', include(admin.site.urls)),
    url(r'^$', 'index'),
	url(r'^lauren', 'lauren'),
	url(r'^(?P<active>.*)', 'page'),
)