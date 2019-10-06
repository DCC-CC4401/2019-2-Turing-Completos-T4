from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response

from .forms import IniciarSesionForm


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


def my_profile(request):
    return render(request, 'UserProfile.html')


def my_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
