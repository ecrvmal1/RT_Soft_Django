from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class MainPageView(TemplateView):
    template_name = "mainapp/index.html"


class StaticPageView(TemplateView):
    template_name = "mainapp/static_page.html"