from django.db import models
from django.conf import settings

# Create your models here.
class Task(models.Model):
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,
                                    related_name="task_assigned_to_user")

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                   related_name="task_created_by_user")

    #if a model belongs 2 ForeignKey than,we need to put different related_name
    tittle=models.CharField(max_length=60)
    body=models.TextField(blank=True)
    is_done=models.BooleanField(default=False)
    creation_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.assigned_to)
