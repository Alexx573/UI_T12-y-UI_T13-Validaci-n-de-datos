from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm
import re
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'name', 'surname', 'control_number', 'age', 'tel', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not re.match(r"^[a-zA-Z0-9._%+-]+@utez\.edu\.mx$", email):
            raise forms.ValidationError("El correo electrónico debe ser del dominio @utez.edu.mx.")
        return email

    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        if len(password) < 8:
            raise forms.ValidationError("La contraseña debe tener al menos 8 caracteres.")
        if not re.search(r"[!#$%&?_]", password):
            raise forms.ValidationError("La contraseña debe contener al menos un símbolo (!, #, $, %, &,? o _).")
        if not re.search(r"\d", password):
            raise forms.ValidationError("La contraseña debe contener al menos un número.")
        return password

    def clean_control_number(self):
        control_number = self.cleaned_data.get('control_number')
        pattern = r"^20\d{3}[A-Z]{3}\d{3}$"
        if not re.fullmatch(pattern, control_number):
            raise forms.ValidationError("La matrícula debe seguir el formato: 20243IGS001 (2 dígitos fijos '20', 3 números, 3 letras mayúsculas, 3 números).")

        return control_number
    
    def clean_tel_number(self):
        tel_number = self.cleaned_data.get('tel_number')
        if not re.fullmatch(r"\d{10}", tel_number):
            raise forms.ValidationError("La matrícula debe tener exactamente 10 digitos")
        return tel_number

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
        
class CustomUserLoginForm(AuthenticationForm):
    pass