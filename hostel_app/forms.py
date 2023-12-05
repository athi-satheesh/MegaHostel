from datetime import datetime

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator

from hostel_app.models import Register, User_Student, User_Parent


# registration form
class RegistrationForm(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = Register
        fields = ('username', 'password1', 'password2')


# for_date_of_birth
class DateInput(forms.DateInput):
    input_type = 'date'


# student registration form
class studentRegistrationForm(forms.ModelForm):
    dob = forms.DateField(widget=DateInput)

    def clean_date(self):
        dob = self.cleaned_data['dob']
        if dob > datetime.date.today():
            raise forms.ValidationError("The date cannot be in future!")
        return dob

    CH = (('M', 'Male'), ('F', 'Female'), ('O', 'Other'))
    gender = forms.CharField(widget=forms.RadioSelect(choices=CH))
    DCH = (('initial', 'Select Department'), ('BArch', 'Architectural'), ('BT', 'Biotechnology'), ('CE', 'Civil'),
           ('CS', 'Computer Science'),
           ('CH', 'Chemical'), ('EE', 'Electrical'), ('ME', 'Mechanical'))
    department = forms.ChoiceField(choices=DCH)
    contact_number = forms.CharField(max_length=10, validators=[RegexValidator(
        '^(?:(?:\+|0{0,2})91(\s*[\ -]\s*)?|[0]?)?[789]\d{9}|(\d[ -]?){10}\d$',
        message="Enter a valid Indian phone number")])
    emergency_contact_number = forms.CharField(max_length=10, validators=[RegexValidator(
        '^(?:(?:\+|0{0,2})91(\s*[\ -]\s*)?|[0]?)?[789]\d{9}|(\d[ -]?){10}\d$',
        message="Enter a valid Indian phone number")])

    class Meta:
        model = User_Student
        fields = ('name', 'dob', 'gender', 'address', 'reg_no', 'department', 'contact_number', 'email',
                  'emergency_contact_number',
                  'photo')


# parent registration form
class parentRegistrationForm(forms.ModelForm):
    CH = (('M', 'Male'), ('F', 'Female'), ('O', 'Other'))
    gender = forms.CharField(widget=forms.RadioSelect(choices=CH))
    RCH = (('F', 'Father'), ('M', 'Mother'), ('G', 'Guardian'))
    relationship_with_student = forms.CharField(widget=forms.RadioSelect(choices=RCH))
    contact_number = forms.CharField(max_length=10, validators=[RegexValidator(
        '^(?:(?:\+|0{0,2})91(\s*[\ -]\s*)?|[0]?)?[789]\d{9}|(\d[ -]?){10}\d$',
        message="Enter a valid Indian phone number")])

    class Meta:
        model = User_Parent
        fields = ('name', 'gender', 'address', 'student_reg_no', 'relationship_with_student', 'contact_number',
                  'email',)
