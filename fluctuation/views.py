from django.conf import settings

from fluctuation.models import Cards, History
from django.shortcuts import render

from pygooglechart import Chart
from pygooglechart import SimpleLineChart
from pygooglechart import Axis

import math

def index(request):
    '''Main function for Templates'''
    cards = {}
    mtgsets = Cards.objects.all().values_list('mtgset', flat=True).distinct()

    for s in mtgsets:
        c = Cards.objects.filter(mtgset=s).order_by('name')
        for ca in c:
            ca.average = float(ca.average)
            ca.prev_average = float(ca.prev_average)
        cards[s] = c

    updated = Cards.objects.latest('updated').updated.ctime()

    return render(request, 'index.html', {'mtgsets': mtgsets, 'cards': cards, 'updated': updated})

def history(request):
    if request.method == 'GET':
        if request.GET.has_key('id'):
            cardid = request.GET['id']
        else:
            # else return to main page
            return index(request)

    c = Cards.objects.get(id=cardid)
    h = History.objects.all().filter(card=c).order_by('created')
    chart = getchart(h)

    return render(request, 'history.html', {'history': h, 'card': c, 'chart': chart})

def getchart(history):
    data = []
    created = []
    for h in history:
        data.append(float(h.average))
        created.append(int(h.created.day))

    max_y = int(math.ceil(max(data))) + 1
    min_y = int(math.floor(min(data))) - 1
    chart = SimpleLineChart(550, 225, y_range=[min_y, max_y])
    chart.add_data(data)
    chart.set_colours(['0000FF'])
    #chart.fill_linear_stripes(Chart.CHART, 0, 'CCCCCC', 0.2, 'FFFFFF', 0.2)
    chart.set_grid(0, 25, 5, 5)
    left_axis = range(min_y, max_y + 1, 2)
    left_axis[0] = ''
    chart.set_axis_labels(Axis.LEFT, left_axis)
    chart.set_axis_labels(Axis.BOTTOM, created)
    return chart
