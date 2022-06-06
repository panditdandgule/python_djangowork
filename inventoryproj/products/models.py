from django.db import models

# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=30)
    price=models.PositiveIntegerField()
    vendor=models.CharField(max_length=40)
    is_active=models.BooleanField(default=True)


    class Meta:
        db_table='product'