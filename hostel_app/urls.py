from django.urls import path

from hostel_app import views

urlpatterns = [
    path('', views.new, name="new"),
    path('admin', views.admn, name="admn")
]