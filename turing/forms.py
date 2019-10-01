from django import forms
from .models import *


class IniciarSesionForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario', widget=forms.TextInput(\
        attrs={'size': '15em'}))
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput(\
        attrs={'size': '15em'}))

