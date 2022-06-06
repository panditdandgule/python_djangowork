from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=60)
    age = models.IntegerField()
    pincode = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'employeeinfo'