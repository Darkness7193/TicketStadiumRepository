from django.http import HttpResponse
from django.shortcuts import render
from .models import Match


def index(request):
    return render(request, 'App1/index.html')


def matches(request):
    match = Match.objects.all()
    return render(request, 'App1/matches.html', {'Match': match})
