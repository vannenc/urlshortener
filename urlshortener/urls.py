from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic import RedirectView
from main.views import IndexView
from main.views import TinyUrlRedirectView


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
    url(r'^create$', 'main.views.create_tinyurl', name='create_tinyurl'),
    url(r'^(?P<tinyurl>[a-zA-Z0-9]+)$', TinyUrlRedirectView.as_view(), name='tinyurl'),
    
)


if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
