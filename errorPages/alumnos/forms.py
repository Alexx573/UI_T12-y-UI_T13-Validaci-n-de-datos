from django import forms
from .models import Alumnos

class alumnoForm(forms.ModelForm):
    class Meta:
        ##Definir en que se basa el model
        model = Alumnos
        #definir los campos que se van a mostrar
        fields = ['nombre', 'apellido', 'edad', 'matricula', 'correo']
        #definir los widgets, cómo se deben de ver los campos
        witgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre del alumno'
                }
            ),
            'apellido': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'apellido del alumno'
                }
            ),
            'edad': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'edad del alumno'
                }
            ),
            'matricula': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'matricula del alumno'
                }
            ),
            'correo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Correo del alumno'
                }
            )
        }

        #Etoquetas o labels personalizadas

        labels ={
            'nombre': 'Nombre del alumno',
            'apellido': 'Nombre del apellido',
            'edad': 'Edad de alumno',
            'matriucula': 'matricula del alumno',
            'correo': 'correo del alumno',
            }

        #Mensajes perosnalizados
        error_messages = {
            'nombre': {
                'required': 'El nombre del alumno es requerido'
            },
            'apellido': {
                'required': 'El apellido del alumno es requerido'
            },
            'edad': {
                'required': 'la edad del alumno es requerido',
                'invalid': 'la edad del alumno debe ser un número'
            },
            'matricula': {
                'required': 'la matricula del alumno es requerido'
            },
            'correo': {
                'required': 'El correo del alumno es requerido'
            },
        }
