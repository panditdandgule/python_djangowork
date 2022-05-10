from django import forms
from django.core import validators


# custom validators
def starts_with_d(self, value):
    if value[0].lower() != 'd':
        raise forms.ValidationError('Name should be starts with d | D')


class FeedBackForm(forms.Form):
    name = forms.CharField(validators=[starts_with_d])
    rollno = forms.IntegerField()
    email = forms.EmailField(validators=[validators.EmailValidator()])
    password = forms.CharField(widget=forms.PasswordInput)
    repassword = forms.CharField(label='Reenter password', widget=forms.PasswordInput)
    feedback = forms.CharField(widget=forms.Textarea, validators=[validators.MaxLengthValidator(40),
                                                                  validators.MinLengthValidator(10)])
    bot_handler=forms.CharField(required=False,widget=forms.HiddenInput)


    # single clean method
    def clean(self):
        print("Total form validation")
        total_cleaned_data = super().clean()
        inputname = total_cleaned_data['name']
        if inputname[0].lower() != 'd':
            raise forms.ValidationError('Name parameter should be start with d')
        inputrollno = total_cleaned_data['rollno']
        if inputrollno <= 0:
            raise forms.ValidationError("Roll no should be >0")
        print("Validating password match")

        fpwd = total_cleaned_data['password']
        spwd = total_cleaned_data['rpassword']
        if fpwd != spwd:
            raise forms.ValidationError('Both passwords must be matched')

        bot_handler_value=total_cleaned_data['bot_handler']
        if len(bot_handler_value)>0:
            raise forms.ValidationError("Request form BOT... cannot be submitted")
    '''
    def clean_name(self):
        print("Validating name")
        inputname=self.cleaned_data['name']
        if len(inputname)<4:
            raise forms.ValidationError("The minimum no of characters in the name should be 4")
        return inputname

    def clean_rollno(self):
        inputrollno=self.cleaned_data['rollno']
        print("Validating roll no")
        return inputrollno

    def clean_email(self):
        inputemail=self.cleaned_data['email']
        print("Validating email field")
        return inputemail

    def clean_feedback(self):
        inputfeedback=self.cleaned_data['feedback']
        print("Validating Feedback field")
        return inputfeedback
    '''
