from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee


# Create your views here.
def emp(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/show')

    else:
        form = EmployeeForm()

    return render(request, 'index.html', {'form': form})


def show(request):
    employees = Employee.objects.all()
    return render(request, 'show.html', {"employees": employees})


def edit(request, eid):
    employees = Employee.objects.get(eid=eid)
    return render(request, 'edit.html', {'employees': employees})


def update(request, eid=None):
    employees = Employee.objects.get(eid=eid)
    form = EmployeeForm(request.POST, instance=employees)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request, 'edit.html', {'employees': employees})


def destroy(request, eid):
    employees = Employee.objects.get(eid=eid)
    employees.delete()
    return redirect("/show")
