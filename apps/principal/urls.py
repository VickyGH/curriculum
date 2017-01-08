from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', inicio.as_view(), name='Inicio'),
]