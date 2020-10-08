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

    specific_location = TextField(blank=True)

    running = BooleanField(default=False)
    chasing = BooleanField(default=False)
    climbing = BooleanField(default=False)
    eating = BooleanField(default=False)
    foraging = BooleanField(default=False)
    other_activities = TextField(blank=True)

    kuks = BooleanField(default=False)
    quaas = BooleanField(default=False)
    moans = BooleanField(default=False)
    tail_flags = BooleanField(default=False)
    tail_twitches = BooleanField(default=False)
    approaches = BooleanField(default=False)
    indifferent = BooleanField(default=False)
    runs_from = BooleanField(default=False)




