from django.db import models

# Create your models here.
class Employee(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    age=models.IntegerField()
    phone=models.BigIntegerField()
    dob=models.DateField()
    email=models.CharField(max_length=40,null=True)
    address=models.CharField(max_length=200)
    pincode=models.IntegerField()
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.firstname

    class Meta:
        db_table='employee'