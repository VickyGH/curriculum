from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import TemplateView

class inicio(TemplateView):
    template_name ="principal/inicioCV.html"