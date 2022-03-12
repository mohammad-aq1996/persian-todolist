from django.urls import reverse_lazy
from .forms import UserCreateForm, ToDoForm
from .models import ToDo
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


class SignUpView(CreateView):
    """
        Signup view with the use of Django built-in signup view
        After signing up successfully user will automatically redirect to the login page
    """
    form_class = UserCreateForm
    success_url = reverse_lazy('todo_app:login')
    template_name = 'signup.html'


class ToDoCreate(LoginRequiredMixin, CreateView):
    """
        Login is required for this view, if the user isn't logged in he/she will automatically redirect to the login page
        Creating new to-do list with these options: 'title', 'content', 'important', and 'completed'
        After adding successfully new to-do list user will automatically redirect to the relevant detail page
        I initial form user field to current User to specify each to-do list belongs to which one
    """
    login_url = '/login/'
    redirect_field_name = 'next'

    form_class = ToDoForm
    template_name = 'todo_form.html'

    def get_initial(self):
        initial = super(ToDoCreate, self).get_initial()
        initial.update({'user': self.request.user})
        return initial


class ToDoListView(LoginRequiredMixin, ListView):
    """
       Login is required for this view, if the user isn't logged in he/she will automatically redirect to the login page
       Returns number and list of to-do list's users that isn't completed
       On every page user will see 2 lists of to-do list
   """
    login_url = '/login/'
    redirect_field_name = 'next'

    model = ToDo
    template_name = 'todolist.html'
    context_object_name = 'todo_list'
    paginate_by = 2

    def get_queryset(self):
        return self.model.objects.filter(user__username=self.request.user, completed__isnull=True).order_by('-created')

    def get_context_data(self, **kwargs):
        context = super(ToDoListView, self).get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        return context


class ToDoCompletedList(ToDoListView):
    """
        This class inherit from ToDoListView
        Returns number and list of to-do list's users that completed
    """

    def get_queryset(self):
        return self.model.objects.filter(user__username=self.request.user, completed__isnull=False).order_by('-completed')

    def get_context_data(self, **kwargs):
        context = super(ToDoListView, self).get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        context['completed'] = True
        return context


class ToDoDetailView(LoginRequiredMixin, DetailView):
    """
       Login is required for this view, if user isn't logged in he/she will automatically redirect to login page
       Returns detail of a specific to do list
   """
    login_url = '/login/'
    redirect_field_name = 'next'

    model = ToDo
    template_name = 'detail.html'
    context_object_name = 'todo'


class ToDoUpdateView(LoginRequiredMixin, UpdateView):
    """
       Login is required for this view, if user isn't logged in he/she will automatically redirect to login page
       With this class users can update their to-do lists and save them.
       This class uses the same template as creating a to-do list
   """
    login_url = '/login/'
    redirect_field_name = 'next'

    form_class = ToDoForm
    template_name = 'todo_form.html'
    model = ToDo


class ToDoDeleteView(LoginRequiredMixin, DeleteView):
    """
        Login is required for this view, if user isn't logged in he/she will automatically redirect to login page
        With this class users can delete their to do lists.

    """
    login_url = '/login/'
    redirect_field_name = 'next'

    model = ToDo
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('todo_app:list')








