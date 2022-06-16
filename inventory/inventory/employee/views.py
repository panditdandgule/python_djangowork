from django.shortcuts import render
from .models import Employee

# Create your views here.
def welcome_page(request):
    return render(request,'employees\welcome.html')

def add_employee(request):
    pass

def list_employee(request):
    emplist=Employee.objects.all()
    return render(request,'employees/show.html', {'emplist':emplist})

def edit_employee(request,eid):
    pass

def delete_employee(request,eid):
    pass