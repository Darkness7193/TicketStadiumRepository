from django.urls import path

from .views import logIn, signIn, logOut


urlpatterns = [
    path('logIn/', logIn, name='logIn'),
    path('signIn/', signIn, name='signIn'),
    path('logOut/', logOut, name='logOut'),
]