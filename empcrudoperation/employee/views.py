from django.http import HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from .models import Employee

# Create your views here.
def welcome(request):
    return render(request,'welcome.html')


def add_employee(request):
    if request.method=='POST':
        formdata= request.POST
        employee=Employee(firstname=formdata['firstname'],
                          lastname=formdata['lastname'],
                          age=formdata['age'],
                          phone=formdata['phone'],
                          dob=formdata['dob'],
                          email=formdata['email'],
                          address=formdata['address'],
                          pincode=formdata['pincode'])

        employee.save()

    return render(request,'add.html')

def list_employee(request):
    employees=Employee.objects.filter(is_active=True).all()
    return render(request,'list_employee.html',{"employees":employees})

def update_employee(request,eid):
    if request.method=='POST':
        formdata=request.POST
        employee = None
        employee=Employee.objects.filter(id=eid).first()

        if employee:
            return HttpResponseRedirect('/edit_employee')
        else:
            employee.firstname=formdata.get('firstname')
            employee.lastname = formdata.get('lastname')
            employee.age = formdata.get('age')
            employee.phone = formdata.get('phone')
            employee.dob = formdata.get('dob')
            employee.email = formdata.get('email')
            employee.address = formdata.get('address')
            employee.pincode = formdata.get('pincode')
            employee.save()
            employee=Employee.objects.filter(is_active=True).all()
            return render(request,'list_employee.html',{'employee':employee})
    return render(request,'update_employee.html')

def edit_employee(request, eid):
    employee = get_object_or_404(Employee, pk=eid)
    context = {
        'employee': employee
    }
    return render(request, 'update_employee.html', context)

def delete_employee(request,eid):
    employee=get_object_or_404(Employee,pk=eid)
    if employee:
        employee.is_active=False
        employee.save()
        employee=Employee.objects.filter(is_active=True).all()
        return render(request,'list_employee.html',{'employees':employee})