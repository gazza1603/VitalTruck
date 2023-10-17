import csv
from django.core.management.base import BaseCommand
from vital_app.models import Vehicle

class Command(BaseCommand):
    help = 'Import vehicle data from CSV'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **options):
        csv_file = options['csv_file']

        with open(csv_file, 'r') as file:
            # Specify the delimiter as a semicolon
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                # Check if the 'status' field is empty in the CSV, and set it to '-notassigned-' if it is
                status = row.get('status', '-notassigned')

                # Map CSV columns to model fields and create new instances
                Vehicle.objects.create(
                    fleet_no=row['fleet_no'],
                    cost_centre=row['cost_centre'],
                    reg_no=row['reg_no'],
                    category=row['category'],
                    group=row['group'],
                    body_type=row['body_type'],
                    status=status,
                    area_available=row.get('area_available', None),  # Leave it empty if CSV field is empty
                )

        self.stdout.write(self.style.SUCCESS('Vehicle data imported successfully.'))


