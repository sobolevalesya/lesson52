from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, reverse, redirect, get_object_or_404
from todo.models import Task, status_choices, TaskType, Status, Type, type_choices, Project
from todo.forms import TaskForm
from django.views.generic import View, CreateView, UpdateView, DetailView, DeleteView


class TaskView(DetailView):
    model = Task
    template_name = "tasks/task_view.html"


def task_view(request, *args, pk, **kwargs):
    task = get_object_or_404(Task, pk=pk)
    return render(request, "tasks/task_view.html", {"task": task})


class TaskCreateView(LoginRequiredMixin, CreateView):
    template_name = 'tasks/task_create.html'
    model = Task
    form_class = TaskForm

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        task = form.save(commit=False)
        task.project = project
        task.save()
        return redirect('todo:project_view', pk=project.pk)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "tasks/task_update.html"
    model = Task
    form_class = TaskForm

    def get_success_url(self):
        return reverse('todo:project_view', kwargs={'pk': self.object.project_id})


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = "tasks/task_delete.html"

    def get_success_url(self):
        return reverse('todo:project_view', kwargs={'pk': self.object.project_id})


    # def get(self, request, *args, **kwargs):
    #     task = get_object_or_404(Task, pk=kwargs.get("pk"))
    #     return render(
    #         request,
    #         "tasks/task_delete.html",
    #         {
    #             "status_choices": status_choices,
    #             "type_choices": type_choices,
    #             "task": task,
    #         },
    #     )

    # def post(self, request, *args, **kwargs):
    #     task = get_object_or_404(Task, pk=kwargs.get("pk"))
    #     task.delete()
    #     return redirect("todo:index")
