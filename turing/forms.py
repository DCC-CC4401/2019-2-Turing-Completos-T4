from django import forms


class IniciarSesionForm(forms.Form):
    username = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'rounded mx-1', 'size': '20em', 'placeholder': "Correo"}))
    password = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={'class': 'rounded mx-1', 'size': '20em', 'placeholder': "Contraseña"}))


class CambiarContrasena(forms.Form):
    old_pass = forms.CharField(label='Contraseña actual', widget=forms.PasswordInput(
        attrs={'class': 'form_control', 'size': '30em', 'placeholder': "***********"}))
    new_pass = forms.CharField(label='Contraseña nueva', widget=forms.PasswordInput(
        attrs={'class': 'form_control', 'size': '30em', 'placeholder': "***********"}))
    confirm_pass = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput(
        attrs={'class': 'form_control', 'size': '30em', 'placeholder': "***********"}))


class ImageUploadForm(forms.Form):
    image = forms.ImageField()
