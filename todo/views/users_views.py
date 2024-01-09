from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import reverse, render, redirect, get_object_or_404
from todo.models import Project
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from todo.forms import TaskForm, SimpleSearchForm, ProjectForm
from django.utils.http import urlencode
from django.db.models import Q


def delete_user(request, project_id, user_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        project = get_object_or_404(Project, pk=project_id)
        project.users.filter(id=user_id).delete()
        return redirect('todo:project_view', pk=project_id)
    user = get_user_model().objects.get(id=user_id)
    return render(request, 'projects/users_delete.html', {'user': user, 'project': project})




