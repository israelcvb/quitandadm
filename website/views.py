from django.views.generic import TemplateView
from django.shortcuts import render


# Create your views here.
class HomeTemplateView(TemplateView):
    template_name = 'website/home.html'
