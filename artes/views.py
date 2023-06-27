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

def edicionProductos(request, codigo):
    productos = Producto.objects.get(codigo=codigo)
    return render(request, "artes/edicionProductos.html", {'productos': productos})

def guardarProducto(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    size = request.POST['txtSize']
    tecnica = request.POST['txtTecnica']
    precio = request.POST['numPrecio']
    imagen = request.FILES['imagenProducto']
    producto = Producto.objects.create(codigo=codigo,nombre=nombre, size=size, tecnica=tecnica, precio=precio, imagen=imagen)
    return redirect('gestionProductos')

def editarProducto(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    size = request.POST['txtSize']
    tecnica = request.POST['txtTecnica']
    precio = request.POST['numPrecio']
    imagen = request.FILES['imagenProducto']

    productos = Producto.objects.get(codigo=codigo)
    productos.nombre = nombre
    productos.size = size
    productos.tecnica = tecnica
    productos.precio = precio
    productos.imagen = imagen
    productos.save()
    return redirect('gestionProductos')
def eliminarProducto(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    producto.delete()
    return redirect('gestionProductos')

def exit(request):
    logout(request)
    return redirect('index')