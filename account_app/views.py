from django.views.generic import CreateView
from .forms import UserCreateForm
from django.urls import reverse_lazy


class SignUpView(CreateView):
    """
        Signup view with the use of Django built-in signup view
        After signing up successfully user will automatically redirect to the login page
    """
    form_class = UserCreateForm
    success_url = reverse_lazy('account_app:login')
    template_name = 'signup.html'
