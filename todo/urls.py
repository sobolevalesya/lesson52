from django.urls import path
from todo.views import index_view, task_create_view, task_view

urlpatterns = [
    path('', index_view, name='index'),
    path('tasks/add/', task_create_view, name='task_create_view'),
    path('task/<int:pk>', task_view, name='task_view')
]

