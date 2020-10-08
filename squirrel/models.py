from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class SquirrelSighting(models.Model):
    latitude = models.FloatField(
        validators=[MinValueValidator(-180), MaxValueValidator(180)],    
    )

    longitude = models.FloatField(
        validators=[MinValueValidator(-180), MaxValueValidator(180)],
    )

    unique_squirrel_id = models.CharField(max_length=50)
    shift = models.CharField(max_length=2)
    date = models.DateField()
    age = models.IntegerField()
    primary_fur_color = models.CharField(max_length=50, blank=True)
    
    GROUND = 'ground plane'
    ABOVE = 'above ground'
    BLANK = ''

    LOCATION_CHOICES = [
        (GROUND, 'Ground Plane'),
        (ABOVE, 'Above Ground'),
        (BLANK, ''),
    ]

    location = models.CharField(
        max_length=50,
        help_text='Whether squirrel was sighted on or above ground level',
        choices=LOCATION_CHOICES,
        default=BLANK,
    )

    specific_location = models.TextField(blank=True)

    running = models.BooleanField(default=False)
    chasing = models.BooleanField(default=False)
    climbing = models.BooleanField(default=False)
    eating = models.BooleanField(default=False)
    foraging = models.BooleanField(default=False)
    other_activities = models.TextField(blank=True)

    kuks = models.BooleanField(default=False)
    quaas = models.BooleanField(default=False)
    moans = models.BooleanField(default=False)
    tail_flags = models.BooleanField(default=False)
    tail_twitches = models.BooleanField(default=False)
    approaches = models.BooleanField(default=False)
    indifferent = models.BooleanField(default=False)
    runs_from = models.BooleanField(default=False)




