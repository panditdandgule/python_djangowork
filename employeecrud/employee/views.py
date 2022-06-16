from django.shortcuts import render
from employee.models import Employee


# Create your views here.
def welcome_page(request):
    return render(request, 'employees/welcome.html')


def list_employees(request):
    emplist = Employee.objects.filter(is_active=True).all()
    return render(request, 'employees\show_list.html', context={"emplist": emplist})


def save_employee(request):
    if request.method == 'POST':
        formdata = request.POST
        eid = formdata.get('eid')
        employee = None
        if eid:
            employee = Employee.objects.filter(id=eid).first()
        if employee:
            employee.first_name = formdata["first_name"]
            employee.last_name = formdata["last_name"]
            employee.age = formdata["age"]
            # employee.gender = formdata["gender"]
            # employee.date_of_birth = formdata["date_of_birth"]
            employee.mobile_number = formdata["mobile_number"]
            employee.email = formdata["email"]
            employee.address = formdata["address"]
            # employee.profileimage = formdata["profileimage"]
            message = "Employee Record Updated successfully"
            emplist = Employee.objects.filter(is_active=True).all()
            return render(request, 'employees/show_list.html', {"emp_list": emplist})
        else:
            employee = Employee(
                first_name=formdata['first_name'],
                last_name=formdata["last_name"],
                age=formdata["age"],
                # gender = formdata["gender"],
                # date_of_birth = formdata["date_of_birth"],
                mobile_number=formdata["mobile_number"],
                email=formdata["email"],
                address=formdata["address"],
                # profileimage = formdata["profileimage"]
            )
            employee.save()
            emplist = Employee.objects.filter(is_active=True).all()
            return render(request, 'employees/show_list.html', {"emp_list": emplist})
    return render(request, 'employees/add.html', {'message': ''})


def edit_employee(request, eid):
    employee = Employee.objects.filter(emp_id=eid).first()
    if employee:
        return render(request, 'employees/edit_employee.html', {"emp": employee})


def delete_employee(request, eid):
    employee = Employee.objects.filter(emp_id=eid).first()
    if employee:
        # employee.delete()  # hard delete
        employee.is_active = False
        employee.save()
        emplist = Employee.objects.filter(is_active=True).all()
        return render(request, 'employees/show_list.html', {"emp_list": emplist})
