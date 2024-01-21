from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.db.models import Q
from django.shortcuts import render, redirect

from hostel_app.forms import RegistrationForm, studentRegistrationForm, parentRegistrationForm, WeeklyFoodForm, \
    NotificationForm, FeedbackForm, ReplyFeedbackForm, CreateRoomForm, VacancyForm
from hostel_app.models import User_Student, User_Parent, Register, Weekly_Food, Notification, Feedback, CreateRoom, \
    Vacancy, BookBedAppointment


# Create your views here.
def new(request):
    return render(request, "index.html")


def admin_view(request):
    return render(request, "admin/index_admin.html")


# registration_for_student
def stud_register(request):
    reg_form = RegistrationForm()
    stud_reg_form = studentRegistrationForm()
    if request.method == "POST":
        reg_form = RegistrationForm(request.POST)
        stud_reg_form = studentRegistrationForm(request.POST, request.FILES)
        if reg_form.is_valid() and stud_reg_form.is_valid():
            stud_reg = reg_form.save(commit=False)
            stud_reg.is_student = True
            stud_reg.save()
            reg = stud_reg_form.save(commit=False)
            reg.user = stud_reg
            reg.save()
            return redirect('login1')
    return render(request, "student/student_RegistrationForm.html", {'reg_form': reg_form, 'stud_form': stud_reg_form})


# registration_for_parent
def parent_register(request):
    reg_form = RegistrationForm()
    parent_reg_form = parentRegistrationForm()
    if request.method == 'POST':
        reg_form = RegistrationForm(request.POST)
        parent_reg_form = parentRegistrationForm(request.POST)
        if reg_form.is_valid() and parent_reg_form.is_valid():
            parent_reg = reg_form.save(commit=False)
            parent_reg.is_parent = True
            parent_reg.save()
            reg = parent_reg_form.save(commit=False)
            reg.user = parent_reg
            reg.save()
            return redirect('login1')
    return render(request, "parent/parent_RegistrationForm.html",
                  {'reg_form': reg_form, 'parent_form': parent_reg_form})


# login_view
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('base')
            elif user.is_parent:
                return redirect('parent_login')
            elif user.is_student:
                return redirect('student_login')
        else:
            messages.info(request, 'Invalid Credentials')
    return render(request, "loginForm.html")


# student_login
def student_login(request):
    return render(request, "student/student_login.html")


# parent_login
def parent_login(request):
    return render(request, "parent/parent_login.html")


# to_view_student_list_by_admin
def viewStudentList(request):
    data = User_Student.objects.all()
    return render(request, "admin/admins_viewStudList.html", {'data': data})


# to_view_parent_list_by_admin
def viewParentList(request):
    data = User_Parent.objects.all()
    return render(request, "admin/admins_viewParentList.html", {'data': data})


# to_update_student_details_by_admin
def updateStudentDetails(request, id):
    stud_data = User_Student.objects.get(id=id)
    stud_reg_form = studentRegistrationForm(instance=stud_data)
    if request.method == "POST":
        stud_reg_form1 = studentRegistrationForm(request.POST, request.FILES, instance=stud_data)
        if stud_reg_form1.is_valid():
            stud_reg_form1.save()
            return redirect('viewStudList')
    return render(request, "admin/updateStudentDetail.html", {'stud_form': stud_reg_form})


# to_delete_student_details_by_admin
def deleteStudent(request, id):
    if request.method == 'POST':
        delt = User_Student.objects.get(id=id)
        user_detail = delt.user
        delt.delete()
        user_detail.delete()
        return redirect("viewStudList")
    return render(request, "admin/admins_viewStudList.html")


# to_delete_parent_details_by_admin
def deleteParent(request, id):
    if request.method == 'POST':
        delt = User_Parent.objects.get(id=id)
        user_detail = delt.user
        delt.delete()
        user_detail.delete()
        return redirect("viewParentList")
    return render(request, "admin/admins_viewParentList.html")


# manage_weekly_food_menu_by-admin
def manageFoodMenu(request):
    food_form = WeeklyFoodForm()
    if request.method == 'POST':
        food_form = WeeklyFoodForm(request.POST)
        if food_form.is_valid():
            food_form1 = food_form.save(commit=False)
            food_form1.save()
            return redirect('viewFoodMenu')
    return render(request, "admin/Register_FoodMenu.html", {'food_form': food_form})


def viewFoodMenu(request):
    data = Weekly_Food.objects.all().order_by('id').values()
    return render(request, "admin/admins_ViewFoodMenu.html", {'data': data})


def updateFoodMenu(request, id):
    food_data = Weekly_Food.objects.get(id=id)
    food_form = WeeklyFoodForm(instance=food_data)
    if request.method == "POST":
        food_form1 = WeeklyFoodForm(request.POST, instance=food_data)
        if food_form1.is_valid():
            food_form1.save()
            return redirect('viewFoodMenu')
    return render(request, "admin/updateFoodMEnu.html", {'food_form': food_form})


# to-view-food-menu-by-student-and-parent
def viewFoodMenubyUser(request):
    data = Weekly_Food.objects.all().order_by('id').values()
    return render(request, "student/viewWeeklyFoodMenu.html", {'data': data})


def viewFoodMenubyParent(request):
    data = Weekly_Food.objects.all().order_by('id').values()
    return render(request, "parent/viewWeeklyFoodMenu.html", {'data': data})


# to-create-notification-by-admin
def manageNotification(request):
    notification_form = NotificationForm()
    if request.method == 'POST':
        notification_form = NotificationForm(request.POST)
        if notification_form.is_valid():
            notification_form1 = notification_form.save(commit=False)
            notification_form1.save()
            return redirect('viewNotification')
    return render(request, "admin/add_notification.html",
                  {'notification_form': notification_form})


# to-view-notifications-created
def viewNotificationByAdmin(request):
    data1 = Notification.objects.all().order_by('id').values()
    return render(request, "admin/viewNotification.html", {'data1': data1})


# delete-notification-by-admin
def deleteNotification(request, id):
    if request.method == 'POST':
        delt = Notification.objects.get(id=id)
        delt.delete()
        return redirect("viewNotification")
    return render(request, "admin/viewNotification.html.html")


# give-feedback-by-student
def giveFeedback(request):
    feedback_form = FeedbackForm()
    student = request.user
    if request.method == "POST":
        feedback_form = FeedbackForm(request.POST)
        if feedback_form.is_valid():
            feedback_form1 = feedback_form.save(commit=False)
            feedback_form1.user = student
            feedback_form1.save()
            return redirect('viewFeedback')
    return render(request, "student/giveFeedback.html", {'feedback_form': feedback_form})


# view-feedback-by-student-itself
def viewFeedback(request):
    data1 = Feedback.objects.filter(user=request.user).order_by('-date')
    return render(request, "student/viewFeedback.html", {'data1': data1})


# view-feedback-by-admin-given-by-student
def viewFeedbackByAdmin(request):
    data1 = Feedback.objects.all()
    return render(request, "admin/viewFeedbackByAdmin.html", {'data1': data1})


# admins-reply-to-feedback-by-student
def replytoFeedback(request, id):
    data1 = Feedback.objects.get(id=id)
    feedback_form = ReplyFeedbackForm(instance=data1)
    if request.method == "POST":
        feedback_form1 = ReplyFeedbackForm(request.POST, instance=data1)
        if feedback_form1.is_valid():
            feedback_form1.save()
            return redirect('viewFeedbackByAdmin')
    return render(request, "admin/replyFeedback.html", {'feedback_form': feedback_form})


# create_room_and_allocate_students_to_the-room
def createRoom(request):
    room_form = CreateRoomForm()
    if request.method == 'POST':
        room_form = CreateRoomForm(request.POST)
        if room_form.is_valid():
            room_form1 = room_form.save(commit=False)
            room_form1.save()
            return redirect('viewOccupancyByAdmin')
    return render(request, "admin/createRoom.html", {'room_form': room_form})


# view_room_occupancy_by_admin
def viewOccupancybyAdmin(request):
    data1 = CreateRoom.objects.all()
    return render(request, "admin/viewOccupancyByadmin.html", {'data1': data1})


def updateOccupancy(request, id):
    room_data = CreateRoom.objects.get(id=id)
    room_form = CreateRoomForm(instance=room_data)
    if request.method == "POST":
        room_form1 = CreateRoomForm(request.POST, instance=room_data)
        if room_form1.is_valid():
            room_form1.save()
            return redirect('viewOccupancyByAdmin')
    return render(request, "admin/updateRoomOccupancy.html", {'room_form': room_form})


# view-room-by-student-that-is-allocated-by-admin
def viewAllocatedRoom(request):
    try:
        student = request.user.id
        data1 = CreateRoom.objects.get(Q(student1=student) | Q(student2=student) | Q(student3=student))
        return render(request, "student/viewOccupancyBystudent.html", {'data1': data1})
    except CreateRoom.DoesNotExist:
        return render(request, "student/viewOccupancyBystudent.html")


def createVacancy(request):
    vacancy_form = VacancyForm()
    if request.method == 'POST':
        vacancy_form1 = VacancyForm(request.POST)
        if vacancy_form1.is_valid():
            vacancy_form1.save()
            return redirect('viewVacancybyAdmin')
    else:
        vacancy_form = VacancyForm()
    return render(request, "admin/createVacancy.html", {'vacancy_form': vacancy_form})

def viewVacancyByAdmin(request):
    data1 = Vacancy.objects.all()
    return render(request, "admin/viewVacancybyAdmin.html", {'data1': data1})

def deleteVacancybyAdmin(request,id):
    if request.method == 'POST':
        delt = Vacancy.objects.get(id=id)
        delt.delete()
        return redirect("viewVacancybyAdmin")
    return render(request, "admin/viewVacancybyAdmin.html")

def viewVacancy(request):
    data1 = Vacancy.objects.all()
    return render(request, "student/viewBedVacancy.html", {'data1': data1})


def bookBedAppointment(request,id):
    vacancy = Vacancy.objects.get(id=id)
    user = User_Student.objects.get(user=request.user)
    appointment = BookBedAppointment.objects.filter(name=user, number_of_bed_vacancy=vacancy)
    if appointment.exists():
        messages.info(request, 'You Have Already Requested Appointment for this Vacancy')
    else:
        if request.method == 'POST':
            obj = BookBedAppointment()
            obj.name = user
            obj.number_of_bed_vacancy = vacancy
            obj.save()
            messages.info(request, 'Appointment Booked Successfully')
    return render(request, 'student/takeAppointment.html', {'vacancy': vacancy})


def viewBedBookingRequestbyStudent(request):
    data1 = BookBedAppointment.objects.all()
    return render(request, "student/viewBedBookingRequest.html", {"data1": data1})

def viewBookingRequestbyAdmin(request,id):
    requests = BookBedAppointment.objects.filter().order_by('-id')
    if request.method =="POST":
        obj= BookBedAppointment.objects.filter(id=id)
        obj.status = 2
        obj.save()
    return render(request, "admin/viewBookingRequests.html", {"requests":requests})



