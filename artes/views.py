from django.shortcuts import render, redirect
from .models import Producto
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

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

@login_required
def productos(request):
    # Lógica para obtener todos los productos
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, 'artes/productos.html', context)

def exit(request):
    logout(request)
    return redirect('index')