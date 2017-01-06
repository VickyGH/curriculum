from django.conf.urls import url

from .views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', inicio.as_view(), name='Inicio'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)