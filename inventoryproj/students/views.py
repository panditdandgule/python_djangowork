from django.shortcuts import render
from .models import Student


# Create your views here.
def welcome_page(request):
    return render(request, 'students/welcome.html')


def save_students(request):
    if request.method == 'POST':
        formdata = request.POST
        sid = formdata.get('id')
        student = None
        if sid:
            student = Student.objects.filter(id=sid).first()
        if student:
            student.name = formdata['name']
            student.age = formdata['age']
            student.email = formdata['email']
            student.address = formdata['address']
            student.save()
            studlist = Student.objects.filter(is_active=True).all()
            return render(request, 'students/show.html', {'studlist': studlist})
        else:
            student = Student(
                name=formdata['name'],
                age=formdata['age'],
                email=formdata['email'],
                address=formdata['address']
            )
            student.save()
            studlist = Student.objects.filter(is_active=True).all()
            return render(request, 'students/show.html', {'studlist': studlist})
    return render(request, 'students/add.html')


def list_students(request):
    studlist = Student.objects.filter(is_active=True).all()
    return render(request, 'students/show.html', {"studlist": studlist})


def edit_student(request, sid):
    student = Student.objects.filter(id=sid).first()
    return render(request, 'students/edit.html', {'student': student})


def delete_student(request, sid):
    student = Student.objects.filter(id=sid).first()
    if student:
        student.is_active = False
        student.save()
        studlist = Student.objects.filter(is_active=True).all()
        return render(request, 'students/show.html', {"studlist": studlist})
