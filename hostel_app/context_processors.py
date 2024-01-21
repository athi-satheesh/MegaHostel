from hostel_app.models import Notification


def viewNotificationByUser(request):
    notification = Notification.objects.all()
    return  {'notifications': notification}