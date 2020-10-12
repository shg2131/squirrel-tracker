from django.core.management.base import BaseCommand

from squirrel.models import SquirrelSighting

import csv

class Command(BaseCommand):
    help = 'Exports squirrel data to a given file path'
    
    def add_arguments(self, parser):
        parser.add_argument('path', nargs='+', type=str)

    def handle(self, *args, **options):
        if len(options['path']) != 1:
            self.stdout.write(
                self.style.ERROR(f'Usage: python manage.py export_squirrel_data /path/to/file.csv')
            )
            return 
        path = options['path'][0]
        with open(path, 'w') as fp:
            writer = csv.writer(fp)
            keys = ['longitude',
                    'latitude',
                    'unique_squirrel_id',
                    'shift',
                    'date',
                    'age',
                    'primary_fur_color',
                    'location',
                    'specific_location',
                    'running',
                    'chasing',
                    'climbing',
                    'eating',
                    'foraging',
                    'other_activities',
                    'kuks',
                    'quaas',
                    'moans',
                    'tail_flags',
                    'tail_twitches',
                    'approaches',
                    'indifferent',
                    'runs_from',
                   ]
            writer.writerow(keys)
            for obj in SquirrelSighting.objects.all():
                writer.writerow([obj.__dict__[key] for key in keys])

        self.stdout.write(self.style.SUCCESS(f'Successfully exported squirrel data to {path}!'))
