from django.contrib import admin

# Register your models here.

from .models import Notification

class NotificationAdmin(admin.ModelAdmin):
    model = Notification
    list_display = ('__str__', 'is_read', 'group', 'creation_date',)
    list_filter = ('is_read','group',)
    search_fields = ('assigned_to__username',)
    list_editable = ('is_read',)

admin.site.register(Notification,NotificationAdmin)