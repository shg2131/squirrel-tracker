from django.urls import path, re_path

from . import views

app_name = 'squirrel'

urlpatterns = [
    path('', views.index, name='index'),
    path('map/', views.map, name='map'),
    path('sightings/', views.SightingsListView.as_view(), name='sightings-list'),
    path('sightings/add/', views.add_sighting, name='add'), 
    re_path(r'sightings/(?P<unique_squirrel_id>\w+-\w{2}-\d+-\d+)/', views.sightings_detail, name='sightings-detail'),
    path('sightings/stats/', views.stats, name='stats'),
]

