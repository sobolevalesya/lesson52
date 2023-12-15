from django.urls import path
from todo.views import IndexView, task_create_view, TaskView, task_update_view, task_delete_view

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('tasks/add/', task_create_view, name='task_create_view'),
    path('task/<int:pk>', TaskView.as_view(), name='task_view'),
    path('task/<int:pk>/update/', task_update_view, name='task_update_view'),
    path('task/<int:pk>/delete/', task_delete_view, name='task_delete_view')

]

