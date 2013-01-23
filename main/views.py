#! /usr/local/env python
from django.http import HttpResponse
from django.views.generic import TemplateView
from main.models import TinyUrl

class IndexView(TemplateView):
    """ index page """
    template_name='home/index.html'


def index(request):
    return HttpResponse('Hello!')
