from django.conf import settings

from fluctuation.models import Cards
from django.shortcuts import render

def index(request):
    '''Main function for Templates'''

    # Each MTG Set we are reviewing
    mtgsets = Cards.objects.all().values_list('mtgset', flat=True).distinct()

    # The latest Prices for all cards
    cards = Cards.objects.order_by('name')

    return render(request, 'index.html', {'mtgsets': mtgsets, 'cards': cards})
