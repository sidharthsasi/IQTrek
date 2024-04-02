#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "IQTrek.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()



import csv
from django.core.management.base import BaseCommand
from restaurants.models import Restaurant, Cuisine

class Command(BaseCommand):
    help = 'Import restaurants data from CSV'

    def add_arguments(self, parser):
        parser.add_argument('restaurants.csv', type=str)

    def handle(self, *args, **kwargs):
        csv_file = kwargs['restaurants.csv']
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                cuisines = row['cuisines'].split(',')
                restaurant = Restaurant.objects.create(
                    name=row['name'],
                    rating=float(row['rating']),
                    table_booking=bool(int(row['table_booking'])),
                    online_delivery=bool(int(row['online_delivery'])),
                    country_code=row['country_code'],
                    city_code=row['city_code']
                )
                for cuisine in cuisines:
                    cuisine_obj, _ = Cuisine.objects.get_or_create(name=cuisine.strip())
                    restaurant.cuisines.add(cuisine_obj)