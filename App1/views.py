from django.shortcuts import render
from .models import Match, Place, Order, User
'''
import psycopg2
conn = psycopg2.connect(dbname='siteDB', user='Superuser', password='1', host='localhost', port='5433')
cursor = conn.cursor()
execute = cursor.execute
'''

def index(request):
    return render(request, 'App1/index.html')


def focusMatch(request):
    data = request.GET

    context = {
        'focus_match': Match.objects.filter(id=data['focus_match_id'])[0],
        'places': Place.objects.all()
    }
    return render(request, 'App1/focusMatch.html', context)


def matchesPage(request):
    context = {'matches': Match.objects.all()}
    return render(request, 'App1/matchesPage.html', context)


def basket(request):
    match_id = int(request.GET['focus_match_id'])
    place_id = int(request.GET['focus_place_id'])
    new_order = Order(ticket=None,
                  place=Place.objects.get(id=place_id),
                  match=Match.objects.get(id=match_id))
    new_order.save()

    context = {'new_order': new_order}
    return render(request, 'App1/basket.html', context)
