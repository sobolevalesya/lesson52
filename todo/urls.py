from django.urls import path
from django.views.generic import RedirectView
from todo.views.projects_views import IndexView, ProjectView, ProjectUpdateView, ProjectDeleteView, ProjectCreateView
from todo.views.tasks_views import (
    TaskCreateView,
    TaskView,
    TaskUpdateView,
    TaskDeleteView,
)


urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("tasks/", RedirectView.as_view(pattern_name="index")),
    path("project/<int:pk>/tasks/add/", TaskCreateView.as_view(), name="task_add"),
    path("task/<int:pk>", TaskView.as_view(), name="task_view"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="task_update_view"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task_delete_view"),
    path("project/<int:pk>", ProjectView.as_view(), name="project_view"),
    path("project/<int:pk>/update/", ProjectUpdateView.as_view(), name="project_update_view"),
    path("project/<int:pk>/delete/", ProjectDeleteView.as_view(), name="project_delete_view"),
    path("project/add/", ProjectCreateView.as_view(), name="project_add"),
]
