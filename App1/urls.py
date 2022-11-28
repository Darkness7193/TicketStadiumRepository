from django.urls import path

from .views import basket, matchesPage, focusMatch, add_ticket


urlpatterns = [
    path('basket/', basket),
    path('matchesPage/', matchesPage),
    path('focusMatch/', focusMatch),
    path('add_ticket/', add_ticket),
]
