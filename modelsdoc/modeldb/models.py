from django.db import models
from datetime import date

# Create your models here.

class Blog(models.Model):
    name=models.CharField(max_length=100)
    tagline=models.TextField()

    class Meta:
        db_table="blog"

    def __str__(self):
        return self.name

class Author(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()

    class Meta:
        db_table="author"

    def __str__(self):
        return self.name

class Entry(models.Model):
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE)
    headline=models.CharField(max_length=255)
    body_text=models.TextField()
    pub_date=models.DateField()
    mod_date=models.DateField(default=date.today)
    authors=models.ManyToManyField(Author)
    number_of_comments=models.IntegerField(default=0)
    rating=models.IntegerField(default=5)

    class Meta:
        db_table="entry"

    def __str__(self):
        return self.headline

