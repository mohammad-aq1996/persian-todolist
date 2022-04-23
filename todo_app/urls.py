from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'todo_app'
urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    path('post/', views.ToDoCreate.as_view(), name='post'),
    path('list/', views.ToDoListView.as_view(), name='list'),
    path('completed-list/', views.ToDoCompletedList.as_view(), name='competed_list'),
    path('detail/<int:pk>/', views.ToDoDetailView.as_view(), name='detail'),
    path('edit/<int:pk>/', views.ToDoUpdateView.as_view(), name='edit'),
    path('del/<int:pk>/', views.ToDoDeleteView.as_view(), name='delete'),
]
