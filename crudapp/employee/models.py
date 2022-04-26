from django.db import models

# Create your models here.

class Employee(models.Model):
    eid=models.AutoField(primary_key=True)
    ename=models.CharField(max_length=30)
    eemail=models.EmailField()
    econtact=models.CharField(max_length=15)

    class Meta:
        db_table="employee"