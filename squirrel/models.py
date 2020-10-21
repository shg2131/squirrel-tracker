from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class SquirrelSighting(models.Model):
    latitude = models.FloatField(
        validators=[MinValueValidator(-90), MaxValueValidator(90)],    
    )

    longitude = models.FloatField(
        validators=[MinValueValidator(-180), MaxValueValidator(180)],
    )

    unique_squirrel_id = models.CharField(max_length=20)

    AM = 'AM'
    PM = 'PM'
    BLANK = ''

    SHIFT_CHOICES = [
        (AM, 'AM'),
        (PM, 'PM'),
    ]

    shift = models.CharField(
        max_length=50,
        choices=SHIFT_CHOICES,
        default=PM,
    )
    
    date = models.DateField()
    
    ADULT = 'Adult'
    JUVENILE = 'Juvenile'
    
    AGE_CHOICES = [
        (ADULT, 'Adult'),
        (JUVENILE, 'Juvenile'),
        #(BLANK, ''),
    ]

    age = models.CharField(
        max_length=50,
        choices=AGE_CHOICES,
        default=ADULT,
    )

    primary_fur_color = models.CharField(max_length=50, blank=True)
    
    GROUND = 'Ground Plane'
    ABOVE = 'Above Ground'

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
        blank=True,
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
    
    def __str__(self):
        return self.unique_squirrel_id


