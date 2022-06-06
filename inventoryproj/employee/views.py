from django.shortcuts import render
from employee.models import Employee
import datetime
import logging #import loggin library

#Get an instance of a logger
logger=logging.getLogger(__name__)

def welcome_page(request):
    logger.warning("Homepage was accessed at "+str(datetime.datetime.now())+" hours!")
    return render(request, 'welcome.html')


def list_employee(request):
    emplist = Employee.objects.filter(is_active=True).all()
    logger.info("List of Employees was accessed at " + str(datetime.datetime.now()) + " hours!")
    return render(request, 'show.html', {"emplist": emplist})


def save_employee(request):
    if request.method == 'POST':
        formdata = request.POST
        eid = formdata.get('eid')
        employee = None
        if eid:
            employee = Employee.objects.filter(id=eid).first()
        if employee:
            employee.name = formdata['name']
            employee.age = formdata['age']
            employee.pincode = formdata['pincode']
            employee.email = formdata['email']
            employee.address = formdata['address']
            employee.save()
            emplist = Employee.objects.filter(is_active=True).all()
            return render(request, 'show.html', {'emplist': emplist})
        else:
            employee = Employee(
                name=formdata['name'],
                age=formdata['age'],
                pincode=formdata['pincode'],
                email=formdata['email'],
                address=formdata['address'],
            )
            employee.save()
            emplist = Employee.objects.filter(is_active=True).all()
            logger.info("Employee save successfully at " + str(datetime.datetime.now()) + " hours!"+employee.name)
            return render(request, 'show.html', {'emplist': emplist})
    return render(request, 'add.html')


def edit_employee(request, eid):
    employee = Employee.objects.filter(id=eid).first()
    if employee:
        logger.info("Employee data edited at " + str(datetime.datetime.now()) + " hours!" + employee.name)
        return render(request, 'edit.html', {'emp': employee})


def delete_employee(request, eid):
    employee = Employee.objects.filter(id=eid).first()
    if employee:
        employee.is_active = False
        employee.save()
        emplist = Employee.objects.filter(is_active=True).all()

        logger.info("Employee Deleted successfully at " + str(datetime.datetime.now()) + " hours!" + employee.name)
        return render(request, 'show.html', {"emplist": emplist})
