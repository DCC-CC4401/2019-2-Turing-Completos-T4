from django.shortcuts import render


def home(request):
    return render(request, 'LandingPageNotLogged.html')


def landing_page(request):
    return render(request, 'LandingPage.html')


def my_profile(request):
    return render(request, 'UserProfile.html')
