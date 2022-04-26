from django.shortcuts import render,redirect
from .models import Registration
from django.views import View

# Create your views here.
class Register(View):
    def get(self,request):

        return render(request,'enroll/add.html')

    def post(self,request):
        postData=request.POST
        firstname=postData.get('firstname')
        lastname = postData.get('lastname')
        email = postData.get('email')
        password = postData.get('password')
        phone = postData.get('phone')

        # validation
        value = {'firstname': firstname,
                 'lastname': lastname,
                 'email': email,
                 'password':password,
                 'phone': phone,
                 }

        register = Registration(firstname=firstname,
                            lastname=lastname,
                            email=email,
                            password=password,
                            phone=phone,
                            )
        error_message = "Something went wrong"

        # saving
        if not error_message:
            #register.password = make_password(customer.password)
            register.save()
            return redirect('enroll/add.html')
        else:
            data = {
                'error': error_message,
                'values': value,
            }
            return render(request, 'enroll/add.html', data)