from django.contrib import admin
from .models import Person,Student,Teacher
# Register your models here.

admin.site.register(Student)
admin.site.register(Teacher)
