import requests

from django.shortcuts import render
from django.views.generic import TemplateView

def _get_random_cat():
    r = requests.get('https://api.thecatapi.com/v1/images/search')
    print(r.status_code)
    return r.json()

class RandomCat(TemplateView):
    """Display a random cat using The Cat API."""

    template_name = 'cats/randomcat.html'

    def get_context_data(self):
        json = _get_random_cat()
        context = {
            'json_response': json,
            'imgurl': json[0]['url'],
            'id': json[0]['id']
        }
        return context
