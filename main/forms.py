from django import forms
from django.core.validators import URLValidator

class TinyUrlForm(forms.Form):
    url = forms.URLField(required=True,error_messages={'required' : 'A url is required.', 'invalid' : 'The URL is invalid.'})

