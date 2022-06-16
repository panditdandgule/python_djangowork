from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Student


# Create your views here.
def index(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'students/index.html', context)


def add(request):
    return render(request, 'students/add.html')


def insert(request):
    firstname = request.POST.get('firstname')
    lastname = request.POST.get('lastname')
    age = request.POST.get('age')
    student = Student(firstname=firstname,
                      lastname=lastname,
                      age=age)
    student.save()
    return HttpResponseRedirect('/students/')


def edit(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    context = {'student': student}
    return render(request, 'students/edit.html', context)


def update(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    student.firstname = request.POST.get('firstname')
    student.lastname = request.POST.get('lastname')
    student.age = request.POST.get('age')
    student.save()
    return HttpResponseRedirect('/students/')


def delete(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    student.delete()
    return HttpResponseRedirect('/students/')
