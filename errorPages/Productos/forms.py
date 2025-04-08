from django import forms
from .models import Producto

#
class productoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre','precio','imagen','categoria']
        widgets = {
         'nombre': forms.TextInput(
             attrs={
                 'class': 'form-control',
                 'placeholder': 'Nombre del producto'
             }
         ),
         'precio':forms.NumberInput(
             attrs={
                'class': 'form-control',
                'placeholder': 'Precio'
             }
         ),
         'imagen':forms.URLInput(
             attrs={
                'class': 'form-control',
                'placeholder': 'Url de la imagen '
             }
         ),
         'categoria': forms.Select(
             attrs={
                 'class': 'form-control'
             }
         )
        }
        
        # Etiquetas personalizadas
        labels = {
            'nombre': 'Nombre del producto',
            'precio': 'Precio (MXM)',
            'imagen': 'Url de la imagen',
            'categoria': 'Categorias del producto'
        }
        #Mensajes de error
        error_messages = {
            'nombre' : {'required': 'El nombre es obligatorio'},
            'precio': {'required': 'El precio no puede estar vacio',
                       'invalid': 'Ingrese un numero valido '},
            'imagen': {'invalid': 'Ingrese una URL válida'}
        }