from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import JsonResponse

from .models import SquirrelSighting
from .forms import SightingForm

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
    print(unique_squirrel_id)
    sightings_qs = SquirrelSighting.objects.filter(unique_squirrel_id=unique_squirrel_id)
    if len(sightings_qs) == 0:
        return
    context = {
        'sighting': sightings_qs[0],
    }
    return render(request, 'squirrel/squirrelsighting_detail.html', context)

def stats(request):
    sightings = SquirrelSighting.objects.all()
    
    # Total numer of sightings
    num_sightings = len(sightings)
    avg_per_day = num_sightings / len(set([s.date for s in sightings]))
    # avg longitude
    # avg latitude
    avg_long = sum([s.longitude for s in sightings]) / num_sightings
    avg_lat = sum([s.latitude for s in sightings]) / num_sightings

    # adult vs juvenile
    adult_num = sum([1 if s.age == "Adult" else 0 for s in sightings])
    juvenile_num = sum([1 if s.age == "Juvenile" else 0 for s in sightings])
    other_num = num_sightings - adult_num - juvenile_num

    # % AM vs PM
    am_pct = sum([1 if s.shift == "AM" else 0 for s in sightings]) / num_sightings * 100
    pm_pct = sum([1 if s.shift == "PM" else 0 for s in sightings]) / num_sightings * 100
    na_pct = 100 - am_pct - pm_pct

    # % Approaches vs Indifferent vs Runs From
    # Line graph with how many spotted on each day
    context = {
        'num_sightings': num_sightings,
        'avg_per_day': round(avg_per_day, 2),
        'avg_long': round(avg_long, 4),
        'avg_lat': round(avg_lat, 4),
        'adult_num': adult_num,
        'juvenile_num': juvenile_num,
        'other_num': other_num,
        'am_pct': round(am_pct, 2),
        'pm_pct': round(pm_pct, 2),
    }
    return render(request, 'squirrel/stats.html', context)


def add_sighting(request):
    if request.method == 'POST':
        form = SightingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/sightings/')
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = SightingForm()
        context = {
            'form': form,
            }
        return render(request, 'squirrel/add.html', context)

def update_sighting(request, **kwargs):
    sighting = SquirrelSighting.objects.filter(unique_squirrel_id=kwargs['unique_squirrel_id']).first()
    if request.method == 'POST':
        form = SightingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/sightings/')
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = SightingForm()
        context = {
            'form': form,
            }
        return render(request, 'squirrel/squirrelsighting_form.html', context)


class SightingUpdateView(UpdateView):
    model = SquirrelSighting
    form_class = SightingForm
    pk_url_kwarg = 'unique_squirrel_id'
    success_url = '/sightings/'

    def get_object(self):
        return self.model.objects.filter(unique_squirrel_id=self.kwargs['unique_squirrel_id']).first()
