from django.core.management.base import BaseCommand

import pandas as pd

class Command(BaseCommand):
    help = 'Imports data from City of New York squirrel census'
    
    def add_arguments(self, parser):
        parser.add_argument('path', nargs='+', type=str)

    def handle(self, *args, **options):
        if len(options['path']) != 1:
            self.stdout.write(
                self.style.ERROR(f'Usage: python manage.py import_squirrel_data /path/to/file.csv')
            )
            return 
        path = options['path'][0]
        url = 'https://data.cityofnewyork.us/api/views/vfnx-vebw/rows.csv'
        pd.read_csv(url).to_csv(path)

        self.stdout.write(self.style.SUCCESS(f'Successfully saved squirrel data to {path}!'))
