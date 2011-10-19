#!/usr/bin/env python

# setup the Django Mod Env
from django.core.management import setup_environ
import settings
setup_environ(settings)

from fluctuation.models import Cards, History
from urllib2 import urlopen, quote
from re import compile

try:
    latest_count = History.objects.latest('created').runcount
    latest_count = latest_count + 1
except:
    latest_count = 1

for c in Cards.objects.all():
    cardname = quote(c.name)

    print '\nPulling Price for Card: %s' % c.name

    # Pull Price listing
    u = urlopen('http://magic.tcgplayer.com/db/wp-ch.asp?CN=%s' % cardname)
    prices = compile('\$(\d*.\d\d)\r\n[\t]*</div>').findall(u.read())

    # TCG does not return 404 on invalid card names,
    # so we will rely on pulling the 2nd element from list
    try:
        avg = prices[1]
    except IndexError:
        print 'Failed to Pull Price'
        continue

    print 'Average Price is: %s' % avg

    # Add price to table
    h = History(name=c.name, average=avg, runcount=latest_count, info=c)
    h.save()
