from django.shortcuts import render, redirect
from .models import Categoria
from .forms import CategoriaForm  
from django.http import JsonResponse



def agregar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)  # Usa ProductoForm aqu
        if form.is_valid():
            form.save()
            return redirect('ver')  # Redirige a la vista de ver productos
    else:
        form = CategoriaForm()
    return render(request, 'agregar_cat.html', {'form': form})

# Vista para ver productos
def ver_categoria(request):
    categoria = Categoria.objects.all()
    return render(request, 'ver_cat.html', {'categorias': categoria})

def lista_categoria(request):
    categorias = Categoria.objects.all()
    data =[
        {
            'nombre': p.nombre,
            'imagen': p.imagen
        }
        for p in categorias
    ]
    return JsonResponse(data,safe=False)

def json_views(request):
    return render (request, "json_cat.html")

# Create your views here.
import json

#@ csrf_exempt <-- noes seguro
def registrar_categoria(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            nuevo_categoria = Categoria.objects.create(
                nombre = data['nombre'],
                imagen = data['imagen']
            )
            return JsonResponse({
                'mensaje': 'Registro exitoso',
                'id': nuevo_categoria.id
            },status=201 )
        except Exception as e:
            return JsonResponse({
                'error': str(e)
            },status=400)
    return JsonResponse({
            'error':'Metodo no permitido'
            },status=405)