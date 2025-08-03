# want to add the data to the db using custom commands 



from django.core.management.base import BaseCommand
from dataentry.models import Student

class Command(BaseCommand):
    # help text
    help="insert data to the database"

    
    def handle (self,*args,**kwargs):
        #add 1 data 
        # Student.objects.create(roll_no=1,name='Saurabh',age='24')        already inserted

        # add multiple data
        dataset= [
            {'roll_no': 2, 'name': 'Prashant', 'age':22},
            {'roll_no': 3, 'name': 'Ritik', 'age':25},
            {'roll_no': 5, 'name': 'Chitransh', 'age':24}
        ]

        # we'll have to look through this data in order to print this 
        for data in dataset:

            # if record exists in the db then we will not push the record
            roll_no= data['roll_no']
            record_exist=Student.objects.filter(roll_no=roll_no).exists() #returns boolean value

            if not record_exist:
                Student.objects.create(roll_no=data['roll_no'],name=data['name'],age=data['age'])
            else:
                self.stdout.write(self.style.WARNING(f'Student with roll_no {roll_no} already exist!'))


        self.stdout.write(self.style.SUCCESS('Data Inserted Successfully'))

