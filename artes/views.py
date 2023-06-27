from django.shortcuts import render, get_object_or_404
from .models import Producto

# Create your views here.

def index(request):
    context={}
    return render(request, "artes/index.html", context)

def galeria(request):
    context={}
    return render(request, "artes/galeria.html", context)

def mision(request):
    context={}
    return render(request, "artes/mision.html", context)

def registro(request):
    context={}
    return render(request, "artes/registro.html", context)

def productos(request):
    # Lógica para obtener todos los productos
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, 'artes/productos.html', context)
