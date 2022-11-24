from django.urls import path

from .views import basket, matchesPage, focusMatch, add_order


urlpatterns = [
    path('basket/', basket),
    path('matchesPage/', matchesPage),
    path('focusMatch/', focusMatch),
    path('add_order/', add_order),
]
