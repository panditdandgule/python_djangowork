from django.contrib import admin
from demoapp.models import Student

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['sid','sname','age']

admin.site.register(Student,StudentAdmin)