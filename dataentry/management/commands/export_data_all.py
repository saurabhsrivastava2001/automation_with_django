#export data from a model to a file 
from django.core.management.base import BaseCommand
from django.apps import apps
import csv
import datetime


#proposed command - python manage.py export_data_all model_name
class Command(BaseCommand):

    help = ' export data from the student model to a file '

    def add_arguments(self, parser):
        parser.add_argument('model_name',type=str,help='model name')


    def handle (self, * args, ** kwargs):
        
        model_name=kwargs['model_name'].capitalize()

        # fetch the data file from the model database
        # we have to check if our model is in the app or not 
        # loop through all the apps 


        model =None

        for app_config in apps.get_app_configs():
            try:
                model= apps.get_model(app_label=app_config.label,model_name=model_name)
                break
            except LookupError:
                continue

        if not model:
            self.stderr.write(f'model {model_name} not found')
            return 
            

        #fetch the data from the model

        data= model.objects.all()

        

        #generate the datetime 
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

        #define the csv file path

        file_path = f'exported_{model_name}_data_{timestamp}.csv'
        print(file_path)


        # open the file and write the rows of the data in that 
        with open (file_path,'w',newline='') as file: # newline = '' bcz it is default to new line in the all os 
            writer = csv.writer(file)

            #write the csv header

            # print the fields of the model dynamic

            writer.writerow([field.name for field in model._meta.fields]) # _meta has all the info of the model


            #write data rows
            for row in data:
                #writer.writerow(row for field in model._meta.fields) # this will fill all the columns with data 
                writer.writerow(getattr(row,field.name) for field in model._meta.fields) # corrcted version 


        self.stdout.write(self.style.SUCCESS('Data exported successfully'))