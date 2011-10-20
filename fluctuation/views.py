from django.conf import settings

from fluctuation.models import Cards
from django.shortcuts import render

def index(request):
    '''Main function for Templates'''
    cards = {}
    mtgsets = Cards.objects.all().values_list('mtgset', flat=True).distinct()

    for s in mtgsets:
        c = Cards.objects.filter(mtgset=s).order_by('name')
        cards[s] = c

    updated = Cards.objects.latest('updated').updated.ctime()

    return render(request, 'index.html', {'mtgsets': mtgsets, 'cards': cards, 'updated': updated})
