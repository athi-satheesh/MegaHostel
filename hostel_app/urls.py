from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from hostel_app import views
from hostel_app import context_processors

urlpatterns = [
    path('', views.new, name="new"),
    path('base', views.admin_view, name="base"),
    path('studReg', views.stud_register, name="stud_register"),
    path('parentReg', views.parent_register, name="parent_register"),
    path('login1', views.login_view, name="login1"),
    path('parent_login', views.parent_login, name="parent_login"),
    path('student_login', views.student_login, name='student_login'),
    path('viewStudList', views.viewStudentList, name='viewStudList'),
    path('viewParentList', views.viewParentList, name='viewParentList'),
    path('updateStudentDetail/<int:id>/', views.updateStudentDetails, name='updateStudentDetail'),
    path('deleteStudent/<int:id>/', views.deleteStudent, name="deleleStudent"),
    path('deleteParent/<int:id>/', views.deleteParent, name="deleleParent"),
    path('manageFoodMenu', views.manageFoodMenu, name='manageFoodMenu'),
    path('viewFoodMenu', views.viewFoodMenu, name='viewFoodMenu'),
    path('updateFoodMenu/<int:id>/', views.updateFoodMenu, name='updateFoodMenu'),
    path('viewFoodMenubyUser', views.viewFoodMenubyUser, name='viewFoodMenubyUser'),
    path('viewFoodMenubyParent', views.viewFoodMenubyParent, name="viewFoodMenubyParent"),
    path('manageNotification', views.manageNotification, name='manageNotification'),
    path('viewNotification', views.viewNotificationByAdmin, name="viewNotification"),
    path('deleteNotification/<int:id>/', views.deleteNotification, name="deleteNotification"),
    path('giveFeedback', views.giveFeedback, name="giveFeedback"),
    path('viewFeedback', views.viewFeedback, name="viewFeedback"),
    path('viewFeedbackByAdmin', views.viewFeedbackByAdmin, name="viewFeedbackByAdmin"),
    path('replytoFeedback/<int:id>', views.replytoFeedback, name="replytoFeedback"),
    path('createRoom', views.createRoom, name="createRoom"),
    path('viewOccupancyByAdmin', views.viewOccupancybyAdmin, name="viewOccupancyByAdmin"),
    path('updateOccupancy/<int:id>/', views.updateOccupancy, name="updateOccupancy"),
    path('viewAllocatedRoomforStudent',views.viewAllocatedRoom, name="viewAllocatedRoomforStudent"),
    path('createVacancy', views.createVacancy, name="createVacancy"),
    path('viewVacancybyAdmin', views.viewVacancyByAdmin, name="viewVacancybyAdmin"),
    path('deleteVacancybyAdmin/<int:id>/', views.deleteVacancybyAdmin, name="deleteVacancybyAdmin"),
    path('viewVacancy', views.viewVacancy, name="viewVacancy"),
    path('bookBedAppointment/<int:id>/', views.bookBedAppointment, name="bookBedAppointment"),
    path('viewBedBookingRequestbyStudent', views.viewBedBookingRequestbyStudent, name="viewBedBookingRequestbyStudent")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
