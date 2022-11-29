from django.urls import path

from .views import logIn, signIn


urlpatterns = [
    path('logIn/', logIn),
    path('signIn/', signIn),
]