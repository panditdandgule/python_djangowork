import datetime

from django.db import models
import datetime

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=255)
    date_of_birth = models.DateTimeField(null=True, blank=True)
    date_of_joining = models.DateTimeField(null=True, blank=True)
    address = models.TextField()


    class Meta:
        abstract=True

class Student(Person):
    roll_number=models.IntegerField()

    class Meta:
        db_table='studentinfo'

    def __str__(self):
        return f'''{self.name}'''



class Teacher(Person):
    compensesion=models.IntegerField()

    class Meta:
        db_table='teacherinfo'

    def __str__(self):
        return f'''{self.name}'''