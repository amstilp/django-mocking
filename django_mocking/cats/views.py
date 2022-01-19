from django.shortcuts import render
from django.views.generic import TemplateView

class RandomCat(TemplateView):
    """Display a random cat using The Cat API."""

    template_name = 'cats/randomcat.html'
