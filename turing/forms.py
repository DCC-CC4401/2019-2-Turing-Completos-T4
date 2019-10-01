from django import forms
from .models import *


class IniciarSesionForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario')
    password = forms.CharField(label='Contraseña')
