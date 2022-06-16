from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.

class YoutubeVideo(models.Model):
    video =models.FileField(upload_to="youtube")

class BaseModel(models.Model):
    uid=models.UUIDField(default=uuid.uuid4,
                         primary_key=True,
                         editable=False) #uuid is a set of alphnumeric string using as primary key
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta:  #skeleton class inner class
        abstract=True #Treating as base class, it will not create any model table in db

class Colors(BaseModel):
    color_code=models.CharField(max_length=100)

class People(BaseModel):
    name=models.CharField(max_length=100)
    about=models.TextField()
    age=models.IntegerField()
    email=models.EmailField()
    colors=models.ManyToManyField(Colors)

class PeopleAddress(BaseModel):
    people=models.ForeignKey(People,on_delete=models.CASCADE,related_name="address")
    address=models.TextField()

#models.CASCADE- If parent table data delete then child table data also delete
#models.SET_DEFAULT-if parent table data delete then it will set default value
#models.SET_NULL -if parent table data delete then it will set null

