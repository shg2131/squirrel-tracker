from django.core.management.base import BaseCommand

from squirrel.models import SquirrelSighting

import csv
import datetime as dt

class Command(BaseCommand):
    help = 'Imports data from City of New York squirrel census'
    
    def add_arguments(self, parser):
        parser.add_argument('path', nargs='+', type=str)

#    def handle(self, *args, **options):
#        SquirrelSighting.objects.all().delete()
    
    def handle(self, *args, **options):
        if len(options['path']) != 1:
            self.stdout.write(
                self.style.ERROR(f'Usage: python manage.py import_squirrel_data /path/to/file.csv')
            )
            return 
        path = options['path'][0]
        with open(path) as fp:
            reader = csv.reader(fp)
            next(reader)

            str_to_bool = lambda x: (True if x.lower() == 'true' else False) 
            
            for row in reader:
                sighting = SquirrelSighting(
                    longitude=float(row[0]),
                    latitude=float(row[1]),
                    unique_squirrel_id=row[2],
                    shift=row[4],
                    date=dt.datetime.strptime(row[5], '%m%d%Y').date(),
                    age=row[7],
                    primary_fur_color=row[8],
                    location=row[12],
                    specific_location=row[14],
                    running=str_to_bool(row[15]),
                    chasing=str_to_bool(row[16]),
                    climbing=str_to_bool(row[17]),
                    eating=str_to_bool(row[18]),
                    foraging=str_to_bool(row[19]),
                    other_activities=row[20],
                    kuks=str_to_bool(row[21]),
                    quaas=str_to_bool(row[22]),
                    moans=str_to_bool(row[23]),
                    tail_flags=str_to_bool(row[24]),
                    tail_twitches=str_to_bool(row[25]),
                    approaches=str_to_bool(row[26]),
                    indifferent=str_to_bool(row[27]),
                    runs_from=str_to_bool(row[28]),
                    uid=row[2],
                )
                
                unique_id_count = SquirrelSighting.objects.filter(
                    unique_squirrel_id=sighting.unique_squirrel_id
                ).count()
                if unique_id_count > 0:
                    sighting.uid = sighting.unique_squirrel_id + f'-{unique_id_count}'
                
                uid_count = SquirrelSighting.objects.filter(
                    uid=sighting.uid
                ).count()
                if uid_count > 0:
                    continue

                sighting.save()

        self.stdout.write(self.style.SUCCESS(f'Successfully imported squirrel data from {path}!'))
