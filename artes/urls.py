from django.urls import path
from . import views
from .views import exit

urlpatterns = [
    path("index", views.index, name="index"),
    path("galeria", views.galeria, name="galeria"),
    path("mision", views.mision, name="mision"),
    path("registro", views.registro, name="registro"),
    path("productos", views.productos, name="productos"),
    path("logout", exit, name="exit"),
]
