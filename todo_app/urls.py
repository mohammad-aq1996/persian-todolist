from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_view
from . import views

app_name = 'todo_app'
urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(), name='logout'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('post/', views.ToDoCreate.as_view(), name='post'),
    path('list/', views.ToDoListView.as_view(), name='list'),
    path('detail/<int:pk>/', views.ToDoDetailView.as_view(), name='detail'),
]
