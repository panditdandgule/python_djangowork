from django.db import models

# Create your models here.

class Student(models.Model):
    sid=models.IntegerField()
    sname=models.CharField(max_length=40)
    age=models.IntegerField()

    def __str__(self):
        return f'''{self.__dict__}'''

    def __repr__(self):
        return str(self)