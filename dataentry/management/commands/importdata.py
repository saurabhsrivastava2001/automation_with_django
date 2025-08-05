from django.core.management.base import BaseCommand,CommandError
#the model can be in the any app so we will install all the apps 
from django.apps import apps

from dataentry.models import Student

import csv # to work with the csv files 

class Command(BaseCommand):
    help=" inport data from csv file "

    #takes csv file path as the input --
    def add_arguments(self, parser):
        parser.add_argument('file_path',type=str, help=" takes the file path as input ") # first argument given 
        parser.add_argument('model_name',type=str,help='name of the model')

    def handle (self,*args , **kwargs):

        #logic goes here

        file_path= kwargs['file_path']
        model_name= kwargs['model_name'].capitalize()

        #search for the model across all installed apps
        model=None
        for app_config in apps.get_app_configs(): 
            """ will have metadata of all the apps--returns the object that will have attribute --name , verbose
            returns the iterable of all AppConfig instances 
            because inorder to look for the model we have to go in each of the apps 
            we need the label here -- store the actual name 
            """

            # try to search for the model inside the app
            try:
                model=apps.get_model(app_config.label,model_name) # checks for the model in the current app
                break #stop searching once the model has been found
            except LookupError:
                # if we dont get the model then we get the lookup error
                continue # search in the next app
        if not model:
            raise CommandError(f'model {model_name} not found in any app!') #remained none
            

        #with makes sure that the file is cloeed properly 
        with open (file_path,'r') as file:
            reader= csv.DictReader(file) # reads a csv file and retursn an iterator that generates dict for each row of the csv file 
            print(reader) #reader is a dict reader object
            for row in reader:
                
                model.objects.create(**row) # acc to the data in the row ( dict ) macthes the data and creates the object
                self.stdout.write(self.style.SUCCESS("Data inseerted successfully!")) #command line output