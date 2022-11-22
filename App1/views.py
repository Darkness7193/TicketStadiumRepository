from django.shortcuts import render, redirect
from .models import Match, Place, Order, User


def index(request):
    if request.method == 'POST':
        requisites = request.POST.get('requisites')
        user = User(requisites=requisites)
        return redirect('App1/matchesPage/')

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
    data = request.GET
    match_id = data.get('focus_match_id', None)
    place_id = data.get('focus_place_id', None)
    if match_id and place_id:
        new_order = Order(ticket=None,
                      place=Place.objects.get(id=int(place_id)),
                      match=Match.objects.get(id=int(match_id)))
        new_order.save()

    context = {'orders': Order.objects.all()}
    return render(request, 'App1/basket.html', context)
