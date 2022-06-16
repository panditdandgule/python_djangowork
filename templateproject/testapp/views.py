from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
import datetime
from testapp.models import Employee

# Create your views here.
def wish(request):
    date=datetime.datetime.now()
    msg=None
    h=int(date.strftime('%H'))
    if h<12:
        msg="Hello Guest!!! Very Very Good Morning!!!"
    elif h<16:
        msg="Hello Guest!!! Very Very Good Afternoon!!!"
    elif h<21:
       msg= "Hello Guest!!! Very Very Good Evening!!!"
    else:
        msg="Hello Guest!!! Very Very Good Night!!"

    my_dict={'insert_date':date,'insert_msg':msg}
    return render(request,'testapp/wish.html',context=my_dict)

def empdata(request):
    emp_list=Employee.objects.all()
    my_dict={'emp_list':emp_list}
    return render(request,'testapp/emp.html',context=my_dict)



