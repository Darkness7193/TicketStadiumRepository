from django.urls import path

from . import views


urlpatterns = [
    path('basket/', views.basket),
    path('matches/', views.matchesPage),
    path('focusMatch/', views.focusMatch),
]
