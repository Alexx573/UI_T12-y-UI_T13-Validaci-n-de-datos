from django.shortcuts import render,redirect
from requests import request
from .models import Producto
from .forms import productoForm
from django.http import JsonResponse



#AGREGAR PRODUCTO
def agregar_producto(request):
    #Primero checamos como llegamos  esta funcion 
    if request.method == 'POST':
        #LLegamos aqui por el enio de un formulario
        form = productoForm(request.POST) #Genera un formulario lleno de info
        if form.is_valid():
            form.save()
            return redirect('ver')#esto redirije a la vista de producto
    else:
        form = productoForm()
    return render(request, 'agregar.html', {'form':form})

#ver productos
def ver_productos():
    productos = Producto.objects.all()
    return render(request, 'ver.html', {'productos': productos})

def lista_productos(request):
    productos = Producto.objects.all()
    data = [
        {
            'nombre': p.nombre,
            'precio ': p.precio,
            'imagen': p.imagen
        }
        for p in productos
    ]
    return JsonResponse(data, safe=False)




def json_view(request):
    return render(request, 'json.html')

import json

#@ csrf_exempt <-- noes seguro
def registrar_producto(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            nuevo_producto = Producto.objects.create(
                nombre = data['nombre'],
                precio= data['precio'],
                imagen = data['imagen']
            )
            return JsonResponse({
                'mensaje': 'Registro exitoso',
                'id': nuevo_producto.id
            },status=201 )
        except Exception as e:
            return JsonResponse({
                'error': str(e)
            },status=400)
    return JsonResponse({
            'error':'Metodo no permitido'
            },status=405)