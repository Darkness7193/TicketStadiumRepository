from django.urls import path

from .views import basket, matches, places_on_stadium, add_ticket, pay_tickets


urlpatterns = [
    path('basket/', basket, name='basket'),
    path('matches/', matches, name='matches'),
    path('places_on_stadium/', places_on_stadium, name='places_on_stadium'),
    path('add_ticket/', add_ticket, name='add_ticket'),
    path('pay_tickets/', pay_tickets, name='pay_tickets'),
]
