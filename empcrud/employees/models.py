from django.db import models

# Create your models here.
class Employee(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=40)
    age=models.IntegerField()

    def __str__(self):
        return f'''{self.firstname}'''

    class Meta:
        db_table='employee'
