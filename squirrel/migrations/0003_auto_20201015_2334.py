# Generated by Django 3.1.2 on 2020-10-15 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squirrel', '0002_auto_20201015_2333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squirrelsighting',
            name='uid',
            field=models.CharField(max_length=50),
        ),
    ]