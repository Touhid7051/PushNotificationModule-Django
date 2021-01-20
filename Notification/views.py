from django.shortcuts import render
from .models import Notification

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return render(request,'dashboard/notAuth.html')     
    unread_notification_count = request.user.notifications_assigned_to_user.filter(is_read=False).count()
    context = {
        'unread_notification_count':unread_notification_count
    }
    return render(request,'dashboard/index.html', context=context)
    
    