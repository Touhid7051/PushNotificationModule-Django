from django.contrib import admin
from .models import Task
# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    model= Task
    list_display = ('__str__','created_by','is_done','creation_date')
admin.site.register(Task , TaskAdmin)