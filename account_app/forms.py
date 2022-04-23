from .models import User
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):
    """
        Using django built-in user create form for signup users
        form fields: 'username', 'password1', 'password2', 'email'
        password2 is confirms field
    """
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']
        labels = {
            'username': 'نام کاربری',
            'email': 'ایمیل'
        }

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)
        self.fields['password1'].label = 'رمز عبور'
        self.fields['password2'].label = 'تایید رمز عبور'

