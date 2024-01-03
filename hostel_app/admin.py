from django.contrib import admin

from hostel_app import models

# Register your models here.

admin.site.register(models.Register)
admin.site.register(models.User_Student)
admin.site.register(models.User_Parent)
admin.site.register(models.Weekly_Food)
admin.site.register(models.Notification)