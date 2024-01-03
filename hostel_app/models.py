from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import BooleanField


# Create your models here.

class Register(AbstractUser):
    is_parent = BooleanField(default="False")
    is_student = BooleanField(default="False")


# student registration model
class User_Student(models.Model):
    user = models.ForeignKey('Register', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    address = models.TextField(max_length=100)
    reg_no = models.CharField(max_length=10)
    department = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=10)
    email = models.EmailField()
    emergency_contact_number = models.CharField(max_length=10)
    photo = models.FileField(upload_to='documents/')

    # inorder_to_return_register_number_of_student_in_parent_registration_form_as_dropdown
    def __str__(self):
        return f'{self.reg_no} {self.name}'


# parent registration model
class User_Parent(models.Model):
    user = models.ForeignKey('Register', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    address = models.TextField(max_length=150)
    student_reg_no = models.ForeignKey('User_Student',
                                       on_delete=models.DO_NOTHING)  # connecting_student_and_parent_via_reg_num
    relationship_with_student = models.CharField(max_length=10)
    contact_number = models.CharField(max_length=10)
    email = models.EmailField()


# Food-manage-model
class Weekly_Food(models.Model):
    day = models.CharField(max_length=10)
    breakfast = models.CharField(max_length=100)
    lunch = models.CharField(max_length=100)
    dinner = models.CharField(max_length=100)


# Make_Notifications
class Notification(models.Model):
    date_of_information = models.DateField(auto_now=True)
    details = models.CharField(max_length=150)


# Feedback-model-by-student
class Feedback(models.Model):
    user = models.ForeignKey('Register', on_delete=models.CASCADE)
    subject = models.TextField()
    date = models.DateField(auto_now=True)
    reply = models.TextField(null=True, blank=True)
