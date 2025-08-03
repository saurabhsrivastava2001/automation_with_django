from django.core.management.base import BaseCommand

from dataentry.models import Student


class Command(BaseCommand):
    help = ' prints all the data in the database '

    def handle(self, *args, **options):
        
        print("Data printed successfully!")