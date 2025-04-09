from django import forms
from urllib.parse import urlparse

class URLForm(forms.Form):
    original_url = forms.CharField(label='URL', max_length=500)

    def clean_original_url(self):
        original_url = self.cleaned_data['original_url']

        if not (original_url.startswith('http://') or original_url.startswith('https://')):
            original_url = 'https://' + original_url

        parsed_url = urlparse(original_url)

        if not parsed_url.netloc:
            raise forms.ValidationError('Please enter a valid URL, including the domain.')

        return original_url
