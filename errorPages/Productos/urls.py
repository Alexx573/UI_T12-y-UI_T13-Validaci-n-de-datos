from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import *

router = SimpleRouter()
router.register(r'api',ProductoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('agregar/', agregar_productos, name='agregar_productos'),
    path('prueba/', prueba_view, name= 'prueba')
    
]