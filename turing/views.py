from django.contrib import messages
from django.contrib.auth import authenticate, get_user, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import IniciarSesionForm, ImageUploadForm, CambiarContrasena
from .models import UserProfile


def home(request):
    if request.method == 'POST':
        form = IniciarSesionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/landing_page/')
            else:
                return render(request, 'LandingPageNotLogged.html', {'invalid': True, 'form': form})
    else:
        form = IniciarSesionForm()
    return render(request, 'LandingPageNotLogged.html', {'form': form})


@login_required
def landing_page(request):
    return render(request, 'LandingPage.html')


@login_required
def change_password(request, context={}):
    form = CambiarContrasena()
    if request.method == 'POST':
        form = CambiarContrasena(request.POST)
        if form.is_valid():
            new = form.cleaned_data['new_pass']
            confirm = form.cleaned_data['confirm_pass']
            username = request.user.username
            password = form.cleaned_data['old_pass']
            user = authenticate(request, username=username, password=password)
            if user is not None and new == confirm:
                user.set_password(new)
                user.save()
                messages.success(request, 'Su contraseña ha sido cambiada exitosamente.')
            else:
                messages.warning(request, 'Las contraseñas no coinciden, por favor intente de nuevo.')
        else:
            messages.error(request, 'Hubo error en el cambio de contraseña, por favor intente de nuevo.')
    context.update({'form': form})
    return request, context


def my_profile(request):
    try:
        img = 'media/' + UserProfile.objects.get(user=get_user(request)).image.url
    except UserProfile.DoesNotExist:
        img = 'Prototypes/img/default-user-image.png'
    (req, cont) = change_password(request, context={'img': img})
    return render(req, 'UserProfile.html', cont)


def my_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def upload_pic(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            (m, created) = UserProfile.objects.get_or_create(user=get_user(request))
            m.image = form.cleaned_data['image']
            m.save()
            messages.success(request, '¡Su foto de perfil ha sido cambiada con éxito!')
            return HttpResponseRedirect(reverse('my_profile'))
        messages.warning(
            request,
            'Su foto de perfil no cumple los requisitos o no indicó una foto nueva, por favor intente de nuevo'
        )
    return HttpResponseRedirect(reverse('my_profile'))
