from django.http import HttpResponse
from django.shortcuts import render

def matches(request):
    return render(request, 'App1/matches.html')
