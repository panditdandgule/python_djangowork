from django.shortcuts import render
from formapp import forms

# Create your views here.
def feedbackview(request):
    form=forms.FeedBackForm()
    if request.method=='POST':
        form=forms.FeedBackForm()
        if form.is_valid():

            print("Form Validatin is success and printing information")
            # print("Name:",form.cleaned_data['name'])
            # print("Roll No:",form.cleaned_data['rollno'])
            # print("Email:",form.cleaned_data['email'])
            # print("FeedBack:",form.cleaned_data['feedback'])

    return render(request,'formapp/feedback.html',context={'form':form})

