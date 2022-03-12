from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import ToDo
from django import forms
from ckeditor.widgets import CKEditorWidget
from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime


class UserCreateForm(UserCreationForm):
    """
        Using django built-in user create form for signup users
        form fields: 'username', 'password1', 'password2', 'email'
        password2 is confirms field
    """
    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2', 'email']
        labels = {
            'username': 'نام کاربری',
            'email': 'ایمیل'
        }

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)
        self.fields['password1'].label = 'رمز عبور'
        self.fields['password2'].label = 'تایید رمز عبور'


class ToDoForm(forms.ModelForm):
    """
        Form for creating new to-do list
        form fields: 'title', 'content', 'important', and 'completed'

    """
    content = forms.CharField(widget=CKEditorWidget(), label='متن کار')

    class Meta:
        model = ToDo
        fields = ['title', 'content', 'important', 'user', 'completed']
        labels = {
            'title': 'عنوان',
            'content': 'متن',
            'important': 'اهمیت'
        }
        widgets = {'user': forms.HiddenInput()}

    def __init__(self, *args, **kwargs):
        super(ToDoForm, self).__init__(*args, **kwargs)
        self.fields['completed'] = JalaliDateField(label='تاریخ انجام ', widget=AdminJalaliDateWidget, required=False)
