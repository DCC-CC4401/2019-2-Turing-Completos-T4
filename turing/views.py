from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import IniciarSesionForm


def home(request):
    if request.method == 'POST':
        form = IniciarSesionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                print("hola")
                return HttpResponseRedirect('/landing_page/')
    else:
        form = IniciarSesionForm()
    return render(request, 'LandingPageNotLogged.html', {'form': form})


@login_required
def landing_page(request):
    return render(request, 'LandingPage.html')


def my_profile(request):
    return render(request, 'UserProfile.html')




