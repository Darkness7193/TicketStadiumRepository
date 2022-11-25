from django.shortcuts import render
from .forms import LogInForm, SignInForm


def logIn(request):
    context = {'logInForm': LogInForm()}
    return render(request, 'ProfilesApp/logIn.html', context)


def signIn(request):
    context = {'signInForm': SignInForm()}
    return render(request, 'ProfilesApp/signIn.html', context)
