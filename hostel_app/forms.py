from datetime import datetime

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator

from hostel_app.models import Register, User_Student, User_Parent, Weekly_Food, Notification, Feedback, CreateRoom, \
    Vacancy, BookBedAppointment


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


# manage-food
class WeeklyFoodForm(forms.ModelForm):
    DAY = (('initial', 'Select Day'), ('Sunday', 'Sunday'), ('Monday', 'Monday'), ('Tuesday', 'Tuesday'),
           ('Wednesday', ' Wednesday'),
           ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'))
    day = forms.ChoiceField(choices=DAY)

    BMENU = (
        ('initial', 'Select Breakfast'), ('Masala Dosa with Tea/ Coffee/ Milk', 'Masala Dosa with Tea/ Coffee/ Milk'),
        ('Poori Masala with Tea/ Coffee/ Milk', 'Poori Masala with Tea/ Coffee/ Milk'),
        ('Idli with Tea/ Coffee/ Milk', 'Idli with Tea/ Coffee/ Milk'),
        ('Pooha with Tea/ Coffee/ Milk', ' Pooha with Tea/ Coffee/ Milk'),
        ('Maggie with Tea/ Coffee/ Milk', 'Maggie with Tea/ Coffee/ Milk'),
        ('Aloo Paratha with Tea/ Coffee/ Milk', 'Aloo Paratha with Tea/ Coffee/ Milk'),
        ('Chapathi & Chana Masala with Tea/ Coffee/ Milk', 'Chapathi & Chana Masala with Tea/ Coffee/ Milk'),
        ('Bread & Omlette with Tea/ Coffee/ Milk', 'Bread & Omlette with Tea/ Coffee/ Milk'),
        ('Upma with Tea/ Coffee/ Milk', 'Upma with Tea/ Coffee/ Milk'))
    breakfast = forms.ChoiceField(choices=BMENU)

    LMENU = (
        ('initial', 'Select Lunch'), ('Meals', 'Meals'),
        ('Rice and Chicken Curry/ Veg Curry', 'Rice and Chicken Curry/ Veg Curry'),
        ('Rice and Fish Fry/ Veg Curry', 'Rice and Fish Fry/ Veg Curry'),
        ('Chicken / Veg Biryani', ' Chicken / Veg Biryani'), ('Egg / Veg Biryani', 'Egg / Veg Biryani'),
        ('Veg Fried Rice  & Gobi Manchurian', 'Veg Fried Rice  & Gobi Manchurian'),
        ('Ghee Rice & Chicken Curry / Veg Curry', 'Ghee Rice & Chicken Curry / Veg Curry'),
        ('Rice & Aloo', 'Rice & Aloo'), ('Rice & Fish Curry/ Veg Curry', 'Rice & Fish Curry/ Veg Curry'))
    lunch = forms.ChoiceField(choices=LMENU)

    DMENU = (
        ('initial', 'Select Dinner'), ('Chapati and Vegetable Curry', 'Chapati and Vegetable Curry'),
        ('Chapati and Chicken Curry/ Veg Curry', 'Chapati and Chicken Curry/ Veg Curry'),
        ('Chapati and Veg Curry', 'Chapati and Veg Curry'),
        ('Chicken / Veg Biryani', ' Chicken / Veg Biryani'), ('Egg / Veg Biryani', 'Egg / Veg Biryani'),
        ('Veg Fried Rice  & Gobi Manchurian', 'Veg Fried Rice  & Gobi Manchurian'),
        ('Batura & Chicken Curry / Veg Curry', 'Batura & Chicken Curry / Veg Curry'),
        ('Chapati & Aloo', 'Chapati & Aloo'),
        ('Chapati & Fish Fry/ Veg Curry', 'Chapati & Fish Fry/ Veg Curry'))
    dinner = forms.ChoiceField(choices=DMENU)

    class Meta:
        model = Weekly_Food
        fields = ('day', 'breakfast', 'lunch', 'dinner',)


class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ('details',)


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ("subject",)


class ReplyFeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ("subject", "reply",)


class CreateRoomForm(forms.ModelForm):
    class Meta:
        model = CreateRoom
        fields = ("room_no", "student1", "student2", "student3",)


class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ("number_of_bed_vacancy",)


class BookBedForm(forms.ModelForm):
    class Meta:
        model = BookBedAppointment
        fields = ("name", "number_of_bed_vacancy", "status",)
