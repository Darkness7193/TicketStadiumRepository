from django.urls import path

from .views import basket, matchesPage, focusMatch, add_ticket, pay_ticket


urlpatterns = [
    path('basket/', basket, name='basket'),
    path('matchesPage/', matchesPage, name='matchesPage'),
    path('focusMatch/', focusMatch, name='focusMatch'),
    path('add_ticket/', add_ticket, name='add_ticket'),
    path('pay_ticket/', pay_ticket, name='pay_ticket'),
]
