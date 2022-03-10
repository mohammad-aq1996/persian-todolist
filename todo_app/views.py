from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import UserCreateForm
from .models import Users
from django.views.generic import CreateView


class SignUpView(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('todo_app:home')
    template_name = 'signup.html'



















