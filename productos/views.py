from django.shortcuts import render, redirect
from .models import Producto

productos = []

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'listar.html', {'productos': productos})

def agregar_productos(request):

    nombre = request.POST['nombreProducto']
    precio = request.POST['precioProducto']
    cantidad = request.POST['cantidadProducto']
    
    if nombre and precio and cantidad:
        Producto.objects.create(nombre=nombre, precio=precio, cantidad=cantidad)
    return redirect('/')

def eliminar_producto(request, id):
    Producto.objects.get(id=id).delete()
    return redirect('/')

def editar_producto(request, id):
    producto = Producto.objects.get(id=id)
    producto.nombre = request.POST['nombreProducto']
    producto.precio = request.POST['precioProducto']
    producto.cantidad = request.POST['cantidadProducto']
    producto.save()
    return redirect('/')
