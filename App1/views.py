from django.shortcuts import render, redirect
from .models import Match, Place, Ticket
from StadiumTickets.myShortcuts import list_to_queryset


def index(request):
    return render(request, 'App1/index.html')


def focusMatch(request):
    data = request.GET
    focus_match = Match.objects.get(id=int(data['focus_match_id']))
    reserved_places = [ticket.place.pk for ticket in Ticket.objects.filter(match=focus_match)]
    free_places = Place.objects.exclude(pk__in=reserved_places)

    context = {
        'focus_match': focus_match,
        'free_places': list(free_places),
    }
    return render(request, 'App1/focusMatch.html', context)


def matchesPage(request):
    context = {'matches': Match.objects.all()}
    return render(request, 'App1/matchesPage.html', context)


def basket(request):
    if request.method == 'POST':
        del_ticket_id = request.POST.get('del_ticket_id')
        Ticket.objects.filter(id=del_ticket_id).delete()
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

    ticket = Ticket(place=place, match=match)
    ticket.save()
    return redirect('/App1/basket')
