from django.db import models

# Create your models here.

class Student(models.Model):
    roll_no = models.CharField(max_length=15)
    name = models.CharField(max_length=30)
    age = models.IntegerField()

    def __str__(self):
        return self.name