import string
import secrets

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


UNIQUE_ID_LEN = 8


def get_rand_id():
    return ''.join(secrets.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits)
                   for _ in range(UNIQUE_ID_LEN))


class List(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    list_name = models.CharField(max_length=500)
    pub_date = models.DateTimeField(auto_now_add=True)
    unique_view_id = models.CharField(unique=True, max_length=UNIQUE_ID_LEN)

    def save(self, *args, **kwargs):
        unique_id = get_rand_id()
        is_exists = List.objects.filter(unique_view_id=unique_id).exists()
        while is_exists:
            print('is_unique {}, {}'.format(is_exists, unique_id))
            unique_id = get_rand_id()
            is_exists = List.objects.filter(unique_view_id=unique_id).exists()
        self.unique_view_id = unique_id
        super(List, self).save()

    def __str__(self):
        return self.list_name


class Task(models.Model):
    to_list = models.ForeignKey(List, related_name='to_list', on_delete=models.CASCADE)
    task_name = models.CharField(max_length=5000)
    pub_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    unique_view_id = models.CharField(unique=True, max_length=UNIQUE_ID_LEN)

    def save(self, *args, **kwargs):
        unique_id = get_rand_id()
        is_exists = Task.objects.filter(unique_view_id=unique_id).exists()
        while is_exists:
            unique_id = get_rand_id()
            is_exists = Task.objects.filter(unique_view_id=unique_id).exists()
        self.unique_view_id = unique_id
        super(Task, self).save()

    def __str__(self):
        return self.task_name

