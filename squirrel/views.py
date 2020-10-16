from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

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


class SightingsListView(ListView):
    model = SquirrelSighting
    paginated_by = 10 #100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class SightingsDetailView(DetailView):
    model = SquirrelSighting


def sightings_detail(request, unique_squirrel_id):
    sighting = SquirrelSighting.objects.filter(unique_squirrel_id=unique_squirrel_id)[0]
    print(sighting.unique_squirrel_id)
    context = {
        'sighting': sighting,
    }
    return render(request, 'squirrel/squirrelsighting_detail.html', context)
