#! /usr/local/env python
from django.http import HttpResponse
from django.http import Http404
from django.views.generic import TemplateView
from django.views.generic import RedirectView
from main.models import TinyUrl


class IndexView(TemplateView):
    """ index page """
    template_name = 'home/index.html'


class TinyUrlRedirectView(RedirectView):
    """ """

    def get_redirect_url(self, **kwargs):
        """ redirect part"""
        try:

            tinyurl = TinyUrl.objects.get(tiny__exact=kwargs['tinyurl'])
            return tinyurl.url

        except Exception, e:
            raise Http404


def index(request):
    return HttpResponse('Hello!')
