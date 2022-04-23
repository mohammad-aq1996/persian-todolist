from django.db import models
from account_app.models import User
from django.utils import timezone
from django.shortcuts import reverse
from ckeditor.fields import RichTextField
from jalali_date import date2jalali, datetime2jalali


class ToDo(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField()
    important = models.BooleanField(default=False)
    created = models.DateTimeField(default=timezone.now)
    completed = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(User, models.CASCADE, related_name='todos')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('todo_app:detail', kwargs={'pk': self.id})

    def get_jalali_date(self):
        return datetime2jalali(self.created)
