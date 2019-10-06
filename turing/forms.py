from django import forms
from .models import *

class IniciarSesionForm(forms.Form):
    username = forms.CharField(label='', widget=forms.TextInput(\
        attrs={'class': 'rounded mx-1','size': '20em', 'placeholder':"Correo" }))
    password = forms.CharField(label='', widget=forms.PasswordInput(\
        attrs={'class': 'rounded mx-1', 'size': '20em','placeholder':"Contraseña"}))
