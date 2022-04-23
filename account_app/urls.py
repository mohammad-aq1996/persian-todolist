from django.urls import path
from django.contrib.auth import views as auth_view
from . import views

app_name = 'account_app'
urlpatterns = [
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(), name='logout'),
    path('signup/', views.SignUpView.as_view(), name='signup'),

    path('password/change/',
         views.PassChangeView.as_view(template_name='passChange.html'),
         name='password_change'
         ),
    path('password/change/done/',
         auth_view.PasswordChangeDoneView.as_view(template_name='passChaneDone.html'),
         name='password_change_done'
         ),

]
