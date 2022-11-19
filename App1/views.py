from django.shortcuts import render
from .models import Match, Place
import psycopg2

conn = psycopg2.connect(dbname='siteDB', user='Superuser', password='1', host='localhost', port='5433')
cursor = conn.cursor()
execute = cursor.execute


def index(request):
    return render(request, 'App1/index.html')


def focusMatch(request):
    get_focus_match = 'SELECT * FROM match WHERE (id = %s);'
    execute(get_focus_match, (request.GET['focus_match_id'], ))
    focus_match = cursor.fetchone()

    context = {
        'focus_match': focus_match,
        'places': Place.objects.all()
    }
    return render(request, 'App1/focusMatch.html', context)


def matchesPage(request):
    context = {'matches': Match.objects.all()}
    return render(request, 'App1/matchesPage.html', context)


def basket(request):
    context = {
        'focus_match_id': request.GET['focus_match_id'],
        'focus_place_id': request.GET['focus_place_id'],
    }
    return render(request, 'App1/basket.html', context)
