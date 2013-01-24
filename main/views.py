#! /usr/local/env python
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.http import Http404
from django.views.generic import TemplateView
from django.views.generic import RedirectView
from main.models import TinyUrl
from main.forms import TinyUrlForm


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


def create_tinyurl(request):
    """ """
    create_form = TinyUrlForm(request.POST)

    if create_form.is_valid() is True:
        new_tinyurl = TinyUrl(url=create_form.cleaned_data['url'])
        new_tinyurl.save()
        return HttpResponse(request.build_absolute_uri(new_tinyurl.tiny))

    else:
        return HttpResponse('Nope')
