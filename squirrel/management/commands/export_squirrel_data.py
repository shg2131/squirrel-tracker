from django.core.management.base import BaseCommand

import pandas as pd

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
        data = pd.DataFrame() # not sure exactly what data we're supposed to export??
        data.to_csv(path)

        self.stdout.write(self.style.SUCCESS(f'Successfully exported squirrel data to {path}!'))
