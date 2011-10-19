from django.conf import settings

from fluctuation.models import Cards, History
from django.shortcuts import render

def index(request):
    '''Main function for Templates'''

    # Each MTG Set we are reviewing
    mtgsets = Cards.objects.all().values_list('mtgset', flat=True).distinct()

    # The latest Prices for all cards
    latest_count = History.objects.latest('created').runcount
    latest_prices = History.objects.filter(runcount=latest_count).order_by('name')

    previous_count = latest_count - 1

    #if previous_count > 1:
    for p in latest_prices:
        prev = History.objects.filter(runcount=previous_count).filter(info=p.info)
        if len(prev) == 1:
            p.paverage = prev[0].average


    return render(request, 'index.html', {'mtgsets': mtgsets, 'latest_prices': latest_prices})
