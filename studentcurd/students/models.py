from django.db import models

# Create your models here.

class Student(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    age=models.IntegerField()

    class Meta:
        db_table='studentsinfo'

    def __str__(self):
        return f'''{self.firstname,self.lastname}'''