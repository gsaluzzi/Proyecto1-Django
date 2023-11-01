
from inicio.views import inicio, crear_celular, crear_tablet, crear_accesorio, celulares
from django.urls import path

urlpatterns = [
    path('', inicio, name="inicio"),
    # path('paletas/', paletas),
    path('celulares/', crear_celular, name="celulares" ),
    path('tablets/', crear_tablet, name="tablets"),
    path('accesorios/', crear_accesorio, name="accesorios"),
    path('celulares_dispo/', celulares, name="celulares_dispo")
]