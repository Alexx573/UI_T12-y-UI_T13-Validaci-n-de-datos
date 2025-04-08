from django import forms 
from .models import Categoria

class CategoriaForm(forms.ModelForm):  # Corregido el nombre de la clase
    class Meta:
        model = Categoria

        fields = ['nombre', 'imagen']

        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'nombre de la categoria'  
                }
            ),
            'imagen': forms.URLInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'url de la imagen'  
                }
            )
        }

        labels = {
            'nombre': 'Categoria',
            'imagen': 'url de la imagen'
        }

        error_messages = {
            'nombre': {'required': 'el nombre es obligatorio'},
        }
