from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import JsonResponse
from .models import SquirrelSighting
from .forms import AddSightingForm

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


def sightings_detail(request, unique_squirrel_id):
    sighting = SquirrelSighting.objects.filter(unique_squirrel_id=unique_squirrel_id)[0]
    print(sighting.unique_squirrel_id)
    context = {
        'sighting': sighting,
    }
    return render(request, 'squirrel/squirrelsighting_detail.html', context)


def add_sighting(request):
    if request.method == 'POST':
        form = AddSightingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/sightings/')
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = AddSightingForm()
        context = {
            'form': form,
            }
        return render(request, 'squirrel/add.html', context)
