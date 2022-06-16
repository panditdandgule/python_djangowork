from django.shortcuts import render
from modelformapp import forms

# Create your views here.
def student_view(request):
    form=forms.StudentForm
    if request.method=='POST':
        form=forms.StudentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
    return render(request,'modelapp/studentform.html',{'form':form})