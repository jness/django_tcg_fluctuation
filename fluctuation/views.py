from django.conf import settings

from fluctuation.models import Cards, History
from django.shortcuts import render

def index(request):
    '''Main function for Templates'''

    # Each MTG Set we are reviewing
    mtgsets = Cards.objects.all().values_list('mtgset', flat=True).distinct()

    # The latest Prices for all cards
    latest_count = History.objects.latest('created').runcount
    latest_prices = History.objects.filter(runcount=latest_count)

    previous_count = latest_count - 1
    previous_prices = History.objects.filter(runcount=previous_count)

    return render(request, 'index.html', {'mtgsets': mtgsets, 'latest_prices': latest_prices, 'previous_prices': previous_prices})

