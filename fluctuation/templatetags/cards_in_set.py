from django import template
from django.conf import settings

register = template.Library()
@register.filter

def cards_in_set(mtgset, cards):
    return cards[mtgset]
