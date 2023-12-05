from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from hostel_app import views

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
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
