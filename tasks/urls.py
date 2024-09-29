# tasks/urls.py
from django.urls import path
from .views import TaskListView, TaskDetailView, TaskCreateView

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),  # http://127.0.0.1:8000/tasks/
    path('<int:pk>/', TaskDetailView.as_view(), name='task_detail'),  # http://127.0.0.1:8000/tasks/<id>/
    path('create/', TaskCreateView.as_view(), name='task_create'),  # http://127.0.0.1:8000/tasks/create/
]
