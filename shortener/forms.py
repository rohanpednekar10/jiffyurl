from django import forms
from .validators import validate_url
import re

class UrlSubmitForm(forms.Form):
    url = forms.CharField(
        label = '',
        validators = [validate_url],
        widget = forms.TextInput(
            attrs = {
                'placeholder': 'Shorten your link here',
                'class': 'form-control mr-2 form-control-lg',
            }
        )
    )

    def clean_url(self):
        url = self.cleaned_data['url']
        if 'http' in url:
            return url
        return 'http://' + url

class AnalyticsForm(forms.Form):
    short_url = forms.CharField(
        label = '',
        widget = forms.TextInput(
            attrs = {
                'placeholder': 'Paste your Jiffy URL here',
                'class': 'form-control mr-2 form-control-lg',
            }
        )
    )

    def get_shortcode(self):
        short_url = self.cleaned_data['short_url']
        shortcode = re.sub('http://127.0.0.1:8000/', '', short_url)
        return shortcode