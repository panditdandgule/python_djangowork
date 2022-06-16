from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login

from accounts.forms import SignUpForm

# Create your views here.
def signup(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        """
        If the form is valid, a User instance is created with the user = form.save().
         The created user is then passed as an argument to the auth_login function, manually authenticating the user. 
        """
        if form.is_valid():
            user=form.save()
            auth_login(request,user)
            return redirect('home')
    else:
        form=SignUpForm()

    return render(request,'signup.html',{'form':form})