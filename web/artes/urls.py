from django.urls import path
from . import views

urlpatterns = [
    path("index", views.index, name="index"),
    path("galeria", views.galeria, name="galeria"),
    path("mision", views.mision, name="mision"),
    path("registro", views.registro, name="registro"),
    path("ubicacion", views.ubicacion, name="ubicacion"),
]
