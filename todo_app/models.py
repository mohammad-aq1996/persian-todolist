from django.db import models
from django.contrib.auth.models import User, PermissionsMixin


class Users(User, PermissionsMixin):

    def __str__(self):
        return self.username
