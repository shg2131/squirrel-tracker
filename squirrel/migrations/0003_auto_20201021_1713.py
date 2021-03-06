# Generated by Django 3.1.2 on 2020-10-21 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squirrel', '0002_auto_20201020_0246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squirrelsighting',
            name='location',
            field=models.CharField(blank=True, choices=[('Ground Plane', 'Ground Plane'), ('Above Ground', 'Above Ground'), ('', '')], default='', help_text='Whether squirrel was sighted on or above ground level', max_length=50),
        ),
    ]
