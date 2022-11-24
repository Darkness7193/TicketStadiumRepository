from django.shortcuts import render
from ProfilesApp.forms import LogInForm, SignInForm


def logIn(request):
    context = {'logInForm': LogInForm()}
    return render(request, '', context)


def signIn(request):
    context = {'signInForm': SignInForm()}
    return render(request, '', context)
