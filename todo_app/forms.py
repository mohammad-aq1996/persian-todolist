from .models import ToDo
from django import forms
from ckeditor.widgets import CKEditorWidget
from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime


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
