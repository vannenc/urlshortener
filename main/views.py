#! /usr/local/env python
from django.http import HttpResponse
from django.http import Http404
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.views.generic import RedirectView
from main.models import TinyUrl
from main.forms import TinyUrlForm

import json


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

        except Exception:
            raise Http404


def create_tinyurl(request):
    """ """
    create_form = TinyUrlForm(request.POST)
    output = {'url': '', 'error': '', 'tiny': '', 'status': ''}

    if create_form.is_valid() is True:
        new_tinyurl = TinyUrl(url=create_form.cleaned_data['url'])
        new_tinyurl.save()
        output['tiny'] = request.build_absolute_uri(new_tinyurl.tiny)
        output['url'] = new_tinyurl.url
        output['status'] = 'OK'

    else:
        output['error'] = create_form.errors['url'][0]
        output['status'] = 'NOK'  # not ok

    if request.POST.get('format', None) is not None:
        return HttpResponse(json.dumps(output))

    else:
        return render_to_response('home/index.html', {'output': output}, context_instance=RequestContext(request))
