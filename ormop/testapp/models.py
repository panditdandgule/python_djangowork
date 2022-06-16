from django.db import models

# Create your models here.
class Author(models.Model):
   name = models.CharField(max_length=50)

   class Meta:
       db_table='author'

   def __str__(self):
       return f'''{self.name}'''

class Book(models.Model):
   name = models.CharField(max_length=50)
   author = models.ForeignKey(Author,on_delete=models.CASCADE,related_name='books')

   class Meta:
       db_table='book'

   def __str__(self):
       return f'''{self.name,self.author}'''
