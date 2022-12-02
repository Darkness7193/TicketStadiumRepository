from functools import reduce

from django.shortcuts import render, redirect
from .models import Match, Place, Ticket


def index(request):
    return redirect('/App1/matchesPage')


def focusMatch(request):
    data = request.GET
    focus_match = Match.objects.get(id=int(data['focus_match_id']))
    reserved_places = [ticket.place.pk for ticket in Ticket.objects.filter(match=focus_match)]
    free_places = Place.objects.exclude(pk__in=reserved_places)

    if request.method == 'POST':
        form = request.POST
        sector = form.get('sector_search')
        row = form.get('row_search')
        count = form.get('count_search')

        if sector:
            free_places = free_places.filter(sector=sector)
        if row:
            free_places = free_places.filter(row=row)
        if count:
            free_places = free_places.filter(count=count)

    context = {
        'focus_match': focus_match,
        'free_places': free_places,
    }
    return render(request, 'App1/focusMatch.html', context)


def matchesPage(request):
    if request.method == 'POST':
        search_query = request.POST.get('matches_search')
        searched_matches = []

        for match in Match.objects.all():
            m = match.__str__()
            if search_query in m:
                searched_matches.append(match)

    else:
        searched_matches = Match.objects.all()

    context = {'searched_matches': searched_matches}
    return render(request, 'App1/matchesPage.html', context)


def basket(request):
    user_tickets = Ticket.objects.filter(host=request.user)

    if request.method == 'POST':
        del_ticket_id = request.POST.get('del_ticket_id')
        user_tickets.filter(id=del_ticket_id).delete()
        return redirect('/App1/basket', permanent=True)
    else:
        context = {
            'paid_tickets': Ticket.objects.filter(is_paid=True),
            'unpaid_tickets': Ticket.objects.filter(is_paid=False),
        }
        return render(request, 'App1/basket.html', context)


def add_ticket(request):
    place_id = request.GET.get('place_id')
    match_id = request.GET.get('match_id')

    place = Place.objects.get(id=int(place_id))
    match = Match.objects.get(id=int(match_id))

    ticket = Ticket(place=place, match=match, host=request.user)
    ticket.save()
    return redirect('/App1/basket')


def pay_tickets(request):
    tickets = Ticket.objects.filter(host=request.user)
    for ticket in tickets:
        ticket.is_paid = True
        ticket.save()
    return redirect('/App1/basket')

