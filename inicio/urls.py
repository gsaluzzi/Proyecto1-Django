
from inicio.views import inicio, paletas
from django.urls import path

urlpatterns = [
    path('', inicio),
    path('paletas/', paletas),       
]