from django.db import models

# Create your models here.
"""
Many-to-many relationships
To define a many-to-many relationship, use ManyToManyField.

In this example, an Article can be published in multiple Publication objects, 
and a Publication has multiple Article objects:
"""

class Publication(models.Model):
    title=models.CharField(max_length=30)

    class Meta:
        ordering=['title']

    def __str__(self):
        return self.title

class Article(models.Model):
    headline=models.CharField(max_length=30)
    publications=models.ManyToManyField(Publication)

    class Meta:
        ordering=['headline']

    def __str__(self):
        return self.headline
