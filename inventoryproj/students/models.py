from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=40)
    age=models.IntegerField()
    email=models.EmailField()
    address=models.CharField(max_length=30)
    is_active=models.BooleanField(default=True)

    class Meta:
        db_table='student'