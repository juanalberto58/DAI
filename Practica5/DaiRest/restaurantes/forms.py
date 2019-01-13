from django import forms
from django.contrib.auth.models import User
from .models import Plato, Registro

class PlatoForm(forms.ModelForm):
    nombre = forms.CharField(max_length=200,required=True, help_text="Nombre del plato: ")
    alergeno = forms.CharField(max_length=200,required=True, help_text="Tipo de alergeno del plato: ")
    precio = forms.FloatField(required=True, help_text="Precio del plato: ")
    class Meta:
        model = Plato
        fields= ('nombre','alergeno', 'precio')

class RegistroForm(forms.ModelForm):
    username = forms.CharField(max_length=200,required=True, help_text="Nombre de usuario: ")
    password = forms.CharField(max_length=200,required=True, help_text="Contraseña: ")
    dni = forms.FloatField(required=True, help_text="DNI: ")
    class Meta:
        model = Registro
        fields= ('username','password', 'dni')
