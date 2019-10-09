from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response

from .forms import IniciarSesionForm, CambiarContrasena


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
                return render_to_response('LandingPageNotLogged.html', {'invalid': True, 'form': form})
    else:
        form = IniciarSesionForm()
    return render(request, 'LandingPageNotLogged.html', {'form': form})


@login_required
def landing_page(request):
    return render(request, 'LandingPage.html')


@login_required
def change_password(request):
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
                # TODO: hacer que me redirija bien y no que tire 404
                return HttpResponseRedirect(reverse('my_profile'))
            else:
                return render(request, 'UserProfile.html', {'change_form': form, 'wrong_old': True})
    else:
        form = CambiarContrasena()
    return render(request, 'UserProfile.html', {'form': form})


def my_profile(request):
    change_password(request)
    return render(request, 'UserProfile.html')


def my_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
