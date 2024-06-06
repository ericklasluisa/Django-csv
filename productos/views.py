import csv

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Producto
from .forms import SubirCSVForm

productos = []

def listar_productos(request):
    productos = Producto.objects.all()
    form = SubirCSVForm()
    return render(request, 'listar.html', {'productos': productos, 'form': form})

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

def importar_csv(request):
    if request.method == 'POST':
        form = SubirCSVForm(request.POST, request.FILES)
        if form.is_valid():
            archivo_csv = request.FILES['archivo_csv']
            decoded_file = archivo_csv.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file)
            for row in reader:
                Producto.objects.create(
                    nombre=row['nombre'],
                    precio=row['precio'],
                    cantidad=row['cantidad']
                )
            return redirect('/')
    return redirect('/')

def exportar_csv(request):
    productos = Producto.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="productos.csv"'

    writer = csv.writer(response)
    writer.writerow(['id','nombre', 'precio', 'cantidad'])
    for producto in productos:
        writer.writerow([producto.id, producto.nombre, producto.precio, producto.cantidad])

    return response
    