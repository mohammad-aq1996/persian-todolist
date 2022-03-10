from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import ToDo
from django import forms


class UserCreateForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2', 'email']


class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ['title', 'content', 'important', 'user']
