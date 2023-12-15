from django.urls import path
from django.views.generic import RedirectView
from todo.views import (
    IndexView,
    TaskCreateView,
    TaskView,
    TaskUpdateView,
    TaskDeleteView,
)


urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("tasks/", RedirectView.as_view(pattern_name="index")),
    path("tasks/add/", TaskCreateView.as_view(), name="task_create_view"),
    path("task/<int:pk>", TaskView.as_view(), name="task_view"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="task_update_view"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task_delete_view"),
]
