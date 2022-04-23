from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


admin.site.register(User, UserAdmin)

UserAdmin.fieldsets[1][1]['fields'] = ("first_name", "last_name", "email", "address", "phone_no")