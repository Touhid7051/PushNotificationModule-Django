from django.dispatch import receiver
from django.db.models.signals import post_save
from Task.models import Task
from .models import Notification

@receiver(post_save,sender=Task)
def create_notification(*args,**kwargs):
    task=kwargs['instance']
    if kwargs['created']:
        if task.created_by != task.assigned_to:
            Notification.objects.create(assigned_to=task.assigned_to, #to whome the notification will apear
                                        group='c',
                                        body=f"{task.created_by.username} created new task for you! ID: {task.id}",
                                        pk_relation=task.id,
            )
    else:
        if task.created_by != task.assigned_to:
            if task.is_done != task.old_instance.is_done:
                Notification.objects.create(assigned_to=task.created_by,
                                            group='d',
                                            body=f"{task.assigned_to.username} Has changed your assigned  tasks(ID: {task.id}) status to {task.is_done}",
                                            pk_relation=task.id,
                                            )


