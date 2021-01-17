from django.dispatch import receiver
from django.db.models.signals import post_save
from Task.models import Task
from .models import Notification

@receiver(post_save,sender=Task)
def create_notification(*args,**kwargs):
    task=kwargs['instance']
    if kwargs['created']:
        if task.created_by != task.assigned_to:
            Notification.objects.create(assigned_to=task.assigned_to,
                                        group='c',
                                        body=f"{task.created_by.username} created new task for you! ID: {task.id}",
                                        pk_relation=task.id,
            )