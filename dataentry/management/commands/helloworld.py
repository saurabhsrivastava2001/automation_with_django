from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help= "Prints hello world"

    def handle(self, *args, ** kwargs):
        # we write the logic we want to perform
        self.stdout.write('Hello world!')
