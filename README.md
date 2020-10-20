# Squirrel Tracker
Tracking squirrel sightings in Central Park. 
The initial dataset is the 2018 NYC Squirrel Census - publicly available here: https://data.cityofnewyork.us/api/views/vfnx-vebw/rows.csv.

The website allows the user to:
 
- View a map of 100 unique squirrel sightings at ```/map```
- View a list of all recorded sightings at ```/sightings```
- Update an existing sighting at ```/sightings/<unique-squirrel-id>```
- Add a sighting of their own at ```/sightings/add```
- View a few aggregated statistics about the sightings at ```/sightings/stats```

Additionally, we have implemented the following management commands:

- ```import_squirrel_data```
    - Usage: ```$ python manage.py import_squirrel_data /path/to/file.csv```
    - Imports data from the given csv file into a sqlite3 database
- ```export_squirrel_data```
    - Usage: ```$ python manage.py export_squirrel_data /path/to/file.csv```
    - Exports data from the sqlite3 database into a csv file at the specified path

Created by Simon Gee and Omar Al Ismaili for IEOR 4501 at Columbia University.

Group Name: Project 54

UNIs: [shg2131, oha2104]  
