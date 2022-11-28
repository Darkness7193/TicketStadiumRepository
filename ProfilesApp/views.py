from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect

from .models import Profile
from StadiumTickets.myShortcuts import get_or_none


def logIn(request):
    if request.method == 'POST':
        form = request.POST
        username = form.get('username')
        password = form.get('password')
        user = authenticate(username=username, password=password)

        if user:
            request.user = user
            redirect(f'/ProfilesApp/logIn')
        else:
            messages.error(request, 'Неверный ввод')
            return HttpResponseRedirect(request.path_info)

    return render(request, 'ProfilesApp/logIn.html')


def signIn(request):
    if request.method == 'POST':
        form = request.POST
        username = form.get('username')
        password = form.get('password')
        password_conf = form.get('password_conf')
        requisites = form.get('requisites')
        previousURL = request.META.get('HTTP_REFERER')

        haveLogin = get_or_none(User, username=username)

        errors = []
        if password != password_conf:
            errors.append('Введенные пароли не совпадают')
        if haveLogin:
            errors.append('Введенный логин уже используется')

        if errors:
            for error_content in errors:
                messages.error(request, error_content)
            return redirect()
        else:
            user = User(username=username, password=password)
            user.save()
            profile = Profile(user=user, requisites=requisites)
            profile.save()
            return redirect(previousURL)

    return render(request, 'ProfilesApp/signIn.html')
