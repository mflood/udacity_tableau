import csv

neighborhoods = {}

my_n = {'athmar-park': 1,
        'baker': 1,
        'barnum': 1,
        'barnum-west': 1,
        'lincoln-park': 1,
        'mar-lee': 1,
        'sun-valley': 1,
        'valverde': 1,
        'villa-park': 1,
        'west-colfax': 1,
        'westwood': 1,
        }


header_order = ["INCIDENT_ID","OFFENSE_ID","OFFENSE_CODE","OFFENSE_CODE_EXTENSION","OFFENSE_TYPE_ID","OFFENSE_CATEGORY_ID","FIRST_OCCURRENCE_DATE","LAST_OCCURRENCE_DATE","REPORTED_DATE","INCIDENT_ADDRESS","GEO_X","GEO_Y","GEO_LON","GEO_LAT","DISTRICT_ID","PRECINCT_ID","NEIGHBORHOOD_ID","IS_CRIME","IS_TRAFFIC"]
with open("reduced.csv", "w") as output:
    writer = csv.DictWriter(output, fieldnames=header_order)
    writer.writeheader()

    with open("crime.csv", "r") as handle:
        reader = csv.DictReader(handle)
        for line in reader:
            if line['NEIGHBORHOOD_ID'] in my_n:
                writer.writerow(line)

