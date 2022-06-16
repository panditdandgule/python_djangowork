from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from employees.models import Employee


# Create your views here.

def index(request):
    employees = Employee.objects.all()
    context = {
        'employees': employees
    }
    return render(request, 'employees/index.html', context)


def add(request):
    return render(request, 'employees/add.html')


def insert(request):
    firstname = request.POST.get('firstname')
    lastname = request.POST.get('lastname')
    age = request.POST.get('age')
    employees = Employee(firstname=firstname,
                         lastname=lastname,
                         age=age
                         )
    employees.save()
    return HttpResponseRedirect('/employees/')


def edit(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    context = {
        'employee': employee
    }
    return render(request, 'employees/edit.html', context)


def update(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    employee.firstname = request.POST.get('firstname')
    employee.lastname = request.POST.get('lastname')
    employee.age = request.POST.get('age')
    employee.save()
    return HttpResponseRedirect('/employees/')


def delete(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    employee.delete()
    return HttpResponseRedirect('/employees/')
