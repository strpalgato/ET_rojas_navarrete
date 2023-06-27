from django.shortcuts import render, redirect
from .models import Producto
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login

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

def register(request):

    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()
            user = authenticate(username=user_creation_form.cleaned_data["username"], password=user_creation_form.cleaned_data["password1"])
            login(request, user)
            return redirect('index')

    return render(request, "registration/register.html", data)


@login_required
def productos(request):
    # Lógica para obtener todos los productos
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, 'artes/productos.html', context)

@login_required
def gestionProductos(request):
    productos = Producto.objects.all()
    context = {'productos': productos}

    return render(request, "artes/gestionProductos.html", context)

def edicionProductos(request):
    productos = Producto.objects.get(id=id)
    return render(request, "artes/edicionProductos.html", {'productos': productos})

def guardarProducto(request):
    nombre = request.POST['txtNombre']
    size = request.POST['txtSize']
    tecnica = request.POST['txtTecnica']
    precio = request.POST['numPrecio']
    imagen = request.FILES['imagenProducto']
    producto = Producto.objects.create(nombre=nombre, size=size, tecnica=tecnica, precio=precio, imagen=imagen)
    return redirect('gestionProductos')

def editarProducto(request, id):
    id = request.POST['txtId']
    nombre = request.POST['txtNombre']
    size = request.POST['txtSize']
    tecnica = request.POST['txtTecnica']
    precio = request.POST['numPrecio']
    imagen = request.FILES['imagenProducto']

    producto = Producto.objects.get(id=id)
    producto.nombre = nombre
    producto.size = size
    producto.tecnica = tecnica
    producto.precio = precio
    producto.imagen = imagen
    producto.save()
    return redirect('gestionProductos')
def eliminarProducto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return redirect('gestionProductos')

def exit(request):
    logout(request)
    return redirect('index')