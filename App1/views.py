from django.shortcuts import render, redirect
from .models import Match, Place, Order, Sector


def index(request):
    return render(request, 'App1/index.html')


def focusMatch(request):
    data = request.GET

    context = {
        'focus_match': Match.objects.get(id=int(data['focus_match_id'])),
        'places': Place.objects.all(),
        'sectors': Sector.objects.all(),
    }
    return render(request, 'App1/focusMatch.html', context)


def matchesPage(request):
    context = {'matches': Match.objects.all()}
    return render(request, 'App1/matchesPage.html', context)


def basket(request):
    if request.method == 'POST':
        del_order_id = request.POST.get('del_order_id')
        Order.objects.filter(id=del_order_id).delete()
        return redirect('/App1/basket', permanent=True)
    else:
        context = {
            'paid_orders': Order.objects.filter(is_paid=True),
            'unpaid_orders': Order.objects.filter(is_paid=False),
        }
        return render(request, 'App1/basket.html', context)


def add_order(request):
    place_id = request.GET.get('place_id')
    match_id = request.GET.get('match_id')

    place = Place.objects.get(id = int(place_id))
    match = Match.objects.get(id = int(match_id))

    order = Order(place=place, match=match)
    order.save()
    return redirect('/App1/basket')
