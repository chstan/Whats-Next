from django.conf.urls import patterns, include, url
from whatsnext.views import homepage_view

urlpatterns = patterns('',
	(r'^$', homepage_view),
)
