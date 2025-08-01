from django.core.management.base import BaseCommand


#proposed command = python manage.py greeting {Name}
#proposed outtput = Hi! {Name} good morning 
class Command(BaseCommand):

    help= "greetings to the person"

    def add_arguments(self, parser):
        parser.add_argument('name',type=str,help= " specifies the user name")

    def handle(self, *args,**kwargs):
        #write the logic
        name = kwargs['name']
        greeting= f'Hi {name}! good morning'
        # error ----- we can make the error also do the stderr.write( )it shows the error 
        # success warning---- self.stdout.write(self.style.success/warning (greeting))
        self.stdout.write(greeting)