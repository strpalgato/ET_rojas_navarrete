from django.shortcuts import render

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

def ubicacion(request):
    context={}
    return render(request, "artes/ubicacion.html", context)
