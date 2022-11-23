from django.urls import path

from . import views


urlpatterns = [
    path('basket/', views.basket),
    path('matchesPage/', views.matchesPage),
    path('focusMatch/', views.focusMatch),

    path('deleteOrder/', views.deleteOrder),
]
