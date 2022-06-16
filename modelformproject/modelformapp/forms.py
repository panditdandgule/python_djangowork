from django import forms
from modelformapp.models import Student

class StudentForm(forms.ModelForm):
    #fields with validators
    class Meta:
        model=Student
        fields='__all__'