from django.urls import path

from .views import logIn, signIn, logOut


urlpatterns = [
    path('logIn/', logIn),
    path('signIn/', signIn),
    path('logOut/', logOut),
]