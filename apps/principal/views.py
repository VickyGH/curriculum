from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, Te amo Edgar Gustavo. Atte Tu Biscocha :P ")