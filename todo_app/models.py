from django.db import models
from django.contrib.auth.models import User, PermissionsMixin
from django.utils import timezone
from django.shortcuts import reverse


class Users(User, PermissionsMixin):

    def __str__(self):
        return self.username


class ToDo(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    important = models.BooleanField(default=False)
    created = models.DateTimeField(default=timezone.now)
    completed = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(User, models.CASCADE, related_name='todos')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('todo_app:detail', kwargs={'pk': self.id})
