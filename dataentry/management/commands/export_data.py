#export data from a model to a file 
from django.core.management.base import BaseCommand
from django.apps import apps
import csv
from dataentry.models import Student
import datetime


#proposed command to export data from a model Student to a csv file
class Command(BaseCommand):

    help = ' export data from the student model to a file '

    def handle (self, * args, ** kwargs):

        # fetch the data file from the model database
        students= Student.objects.all()
        print(students)

        #generate the datetime 
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

        #define the csv file path

        file_path = f'exported_data_{timestamp}.csv'
        print(file_path)


        # open the file and write the rows of the data in that 
        with open (file_path,'w',newline='') as file: # newline = '' bcz it is default to new line in the all os 
            writer = csv.writer(file)


            #write the csv header
            writer.writerow(['roll_no','name','age'])


            #write data rows
            for student in students:
                writer.writerow([student.roll_no,student.name,student.age]) # with statement will take care of closing the file

        self.stdout.write(self.style.SUCCESS('Data exported successfully'))