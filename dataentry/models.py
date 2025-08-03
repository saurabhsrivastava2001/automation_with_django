from django.db import models

# Create your models here.

class Student(models.Model):
    roll_no = models.CharField(max_length=15)
    name = models.CharField(max_length=30)
    age = models.IntegerField()

    def __str__(self):
        return self.name
    
class Customer(models.Model):
    customer_id=models.IntegerField()
    customer_name= models.CharField(max_length=40)
    country=models.CharField(max_length=30)

    def __str__(self):
        return self.customer_name