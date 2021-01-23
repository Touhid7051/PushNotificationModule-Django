from django.shortcuts import render
from .models import Notification
from django.http import JsonResponse
from django.core import serializers

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
    
    
def get_notification_info(request):
    if not request.user.is_authenticated:
        context = {
            'unreaded_notification_count':'',
            'unreaded_notifications':'',
            'old_notifications':''
        }
        return JsonResponse(context)

    notifications = request.user.notifications_assigned_to_user.order_by('-creation_date')
    old_notifications = notifications.filter(is_read=True)
    unreaded_notifications = notifications.filter(is_read=False).order_by('creation_date')

    context = {
        'unreaded_notification_count':unreaded_notifications.count(),
        'unreaded_notifications':serializers.serialize('json',unreaded_notifications[:5]),
        'old_notifications':serializers.serialize('json',old_notifications[:3])
    }

    return JsonResponse(context)

def mark_notification_as_readed(request):
    if not request.method == 'POST':
        return JsonResponse({})
    if not request.user.is_authenticated:
        return JsonResponse({})
    notifications = request.user.notifications_assigned_to_user
    unreaded_notifications = notifications.filter(is_read=False).order_by('creation_date')[:5]
    for notification in unreaded_notifications:
        notification.is_read = True
        notification.save()
    return JsonResponse({})