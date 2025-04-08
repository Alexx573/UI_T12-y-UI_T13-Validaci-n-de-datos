from .models import Alumnos
from .serializers import AlumnosSerializer
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from .forms import alumnoForm
from django.shortcuts import render

class AlumnosViewSet(viewsets.ModelViewSet):
    queryset = Alumnos.objects.all()
    serializer_class = AlumnosSerializer
    renderer_classes = [JSONRenderer]

def agregar_alumno(request):
    form = alumnoForm()
    return render(request,'gonzalez_Alexander.html', {'form': form})