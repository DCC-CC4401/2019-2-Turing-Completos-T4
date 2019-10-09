from django.contrib import messages
from django.contrib.auth import authenticate, get_user, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import ImageUploadForm, IniciarSesionForm
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


def my_profile(request):
    try:
        img = 'media/' + UserProfile.objects.get(user=get_user(request)).image.url
    except UserProfile.DoesNotExist:
        img = 'Prototypes/img/default-user-image.png'
    return render(request, 'UserProfile.html', context={'img': img})


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
