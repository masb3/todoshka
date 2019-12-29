from django.db import models
from django.contrib.auth.models import User


class Lists(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    list_name = models.CharField(max_length=500)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.list_name


class Tasks(models.Model):
    to_list = models.ForeignKey(Lists, related_name='to_list', on_delete=models.CASCADE)
    task_name = models.CharField(max_length=5000)
    end_date = models.DateTimeField(null=True)
    is_done = models.BooleanField(default=False)

