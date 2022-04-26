from django.db import models

class Registration(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    email=models.EmailField(null=True)
    password=models.CharField(max_length=10)
    phone=models.CharField(max_length=10)

    def __str__(self):
        return self.firstname,self.lastname



