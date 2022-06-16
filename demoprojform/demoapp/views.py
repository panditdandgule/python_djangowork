from django.shortcuts import render
from demoapp import forms
# Create your views here.

def home(request):
    return render(request,'demoapp/home.html')

def studentinputview(request):
    form=forms.StudentForm()
    if request.method=='POST':
        form=forms.StudentForm(request.POST)
        if form.is_valid():
            print("Form validation is success and printing data")
            print("Name",form.cleaned_data['name'])
            print("Marks",form.cleaned_data['marks'])

    return render(request,'demoapp/input.html',{'form':form})

