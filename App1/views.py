from django.http import HttpResponse
from django.shortcuts import render
from .models import Match
import psycopg2

conn = psycopg2.connect(dbname='siteDB', user='Superuser', password='1', host='localhost', port='5433')
cursor = conn.cursor()
execute = cursor.execute

cursor.execute("select relname from pg_class where relkind='r' and relname !~ '^(pg_|sql_)';")
print(list(cursor.fetchall()))


def index(request):
    return render(request, 'App1/index.html')


def focusMatch(request):
    match_name = request.GET['match_name']
    execute('SELECT * FROM match WHERE (name = %s);', (match_name, ))
    match_attrs = cursor.fetchone()

    return render(request, 'App1/focusMatch.html', {'match_data': match_attrs})


def matchesPage(request):
    matches = Match.objects.all()
    return render(request, 'App1/matchesPage.html', {'matches': matches})
