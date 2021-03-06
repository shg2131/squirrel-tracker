# Generated by Django 3.1.2 on 2020-10-19 20:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SquirrelSighting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField(validators=[django.core.validators.MinValueValidator(-180), django.core.validators.MaxValueValidator(180)])),
                ('longitude', models.FloatField(validators=[django.core.validators.MinValueValidator(-180), django.core.validators.MaxValueValidator(180)])),
                ('unique_squirrel_id', models.CharField(max_length=20)),
                ('shift', models.CharField(choices=[('AM', 'AM'), ('PM', 'PM')], default='PM', max_length=50)),
                ('date', models.DateField()),
                ('age', models.CharField(choices=[('Adult', 'Adult'), ('Juvenile', 'Juvenile')], default='Adult', max_length=50)),
                ('primary_fur_color', models.CharField(blank=True, max_length=50)),
                ('location', models.CharField(choices=[('Ground Plane', 'Ground Plane'), ('Above Ground', 'Above Ground'), ('', '')], default='', help_text='Whether squirrel was sighted on or above ground level', max_length=50)),
                ('specific_location', models.TextField(blank=True)),
                ('running', models.BooleanField(default=False)),
                ('chasing', models.BooleanField(default=False)),
                ('climbing', models.BooleanField(default=False)),
                ('eating', models.BooleanField(default=False)),
                ('foraging', models.BooleanField(default=False)),
                ('other_activities', models.TextField(blank=True)),
                ('kuks', models.BooleanField(default=False)),
                ('quaas', models.BooleanField(default=False)),
                ('moans', models.BooleanField(default=False)),
                ('tail_flags', models.BooleanField(default=False)),
                ('tail_twitches', models.BooleanField(default=False)),
                ('approaches', models.BooleanField(default=False)),
                ('indifferent', models.BooleanField(default=False)),
                ('runs_from', models.BooleanField(default=False)),
            ],
        ),
    ]
