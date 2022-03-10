from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import UserCreateForm, ToDoForm
from .models import Users
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


class SignUpView(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('todo_app:home')
    template_name = 'signup.html'


class ToDoCreate(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    # redirect_field_name = 'test.html'

    form_class = ToDoForm
    success_url = reverse_lazy('todo_app:home')
    template_name = 'todo_form.html'

    def get_initial(self):
        initial = super(ToDoCreate, self).get_initial()
        initial.update({'user': self.request.user})
        return initial



















