from django.shortcuts import render

from squirrel.models import SquirrelSighting

import random

def index(request):
    return render(request, 'squirrel/index.html', {})

def map(request):
    sightings = SquirrelSighting.objects.all().order_by('-date')[:100]
    context = {
        'sightings': sightings,
    }
    return render(request, 'squirrel/map.html', context)
