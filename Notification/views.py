from django.shortcuts import render
from .models import Notification

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return render(request,'dashboard/notAuth.html')
    notifications = request.user.notifications_assigned_to_user.order_by('-creation_date')
    old_notifications = notifications.filter(is_read=True)   
    unread_notifications = request.user.notifications_assigned_to_user.filter(is_read=False).order_by('creation_date')
    context = {
        'unread_notification_count':unread_notifications.count(),
        'unread_notifications':unread_notifications[:5],
        'old_notifications':old_notifications[:3]
    }
    return render(request,'dashboard/index.html', context=context)
    
    