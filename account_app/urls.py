from django.urls import path
from django.contrib.auth import views as auth_view
from . import views

app_name = 'account_app'
urlpatterns = [
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(), name='logout'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
]
