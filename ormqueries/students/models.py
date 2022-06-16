from django.db import models

# Create your models here.
class Teacher(models.Model):
    teacher_name=models.CharField(max_length=200)

    class Meta:
        db_table='teacher'

    def __str__(self):
        return f'''{self.teacher_name}'''

class Student(models.Model):
    username=models.CharField(max_length=200)
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    mobile=models.CharField(max_length=10)
    email=models.EmailField()
    teacher_name=models.ForeignKey(Teacher,blank=True,null=True,on_delete=models.CASCADE)

    class Meta:
        db_table='student'

    def __str__(self):
        return "%s %s" %(self.firstname,self.lastname)