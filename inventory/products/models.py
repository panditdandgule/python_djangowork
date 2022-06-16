from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=30)
    price=models.FloatField()
    qty=models.IntegerField()
    vendor_email=models.EmailField()
    vendor_website=models.URLField()
    product_image=models.ImageField(upload_to='resources/')
    product_manf_date=models.DateField()

    class Meta:
        db_table='products'

