from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from main.views import IndexView
from main.models import TinyUrl

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'urlshortener.views.home', name='home'),
    # url(r'^urlshortener/', include('urlshortener.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^(?P<tinyurl>[a-zA-Z0-9]+)$', ),
)
