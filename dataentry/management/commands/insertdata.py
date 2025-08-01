# want to add the data to the db using custom commands 



from django.core.management.base import BaseCommand
from dataentry.models import Student

class Command(BaseCommand):
    # help text
    help="insert data to the database"

    # handle function
    #add 1 data 
    # Student.objects.create(roll_no=1,name='Saurabh',age='24')        already inserted

    # add multiple data
    dataset= [
        {'roll_no': 2, 'name': 'Prashant', 'age':22},
        {'roll_no': 3, 'name': 'Ritik', 'age':25},
        {'roll_no': 4, 'name': 'Prashant', 'age':24}
    ]

    # we'll have to look through this data in order to print this 
    for data in dataset:
        Student.objects.create(roll_no=data['roll_no'],name=data['name'],age=data['age'])

    def handle (self,*args,**kwargs):
        self.stdout.write(self.style.SUCCESS('Data Inserted Successfully'))

