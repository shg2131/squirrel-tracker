from django.urls import path

from . import views

app_name = 'squirrel'

urlpatterns = [
    path('', views.index, name='index'),
    path('map/', views.map, name='map'),
    path('sightings/', views.SightingsListView.as_view(), name='sightings-list'),
    path('sightings/add/', views.add_sighting, name='add'), 
    path('sightings/<str:unique_squirrel_id>/', views.sightings_detail, name='sightings-detail'),
]

