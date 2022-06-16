from django.shortcuts import render
from demoapp.models import Student

# Create your views here.

def student_data(request):
    allstudents=Student.objects.all()
    stud_dict={'allstudents':allstudents}
    return render(request,'demoapp/display.html',context=stud_dict)