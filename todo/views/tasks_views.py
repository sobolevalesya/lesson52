from django.shortcuts import render, reverse, redirect, get_object_or_404
from todo.models import Task, status_choices, TaskType, Status, Type, type_choices, Project
from todo.forms import TaskForm
from django.views.generic import View, TemplateView, CreateView


# class IndexView(View):
#     def get(self, request, *args, **kwargs):
#         tasks = Task.objects.all()
#         return render(request, "projects/index.html", {"tasks": tasks})


class TaskView(TemplateView):
    template_name = "tasks/task_view.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["task"] = get_object_or_404(Task, pk=kwargs.get("pk"))
        return context


def task_view(request, *args, pk, **kwargs):
    task = get_object_or_404(Task, pk=pk)
    return render(request, "tasks/task_view.html", {"task": task})


class TaskCreateView(CreateView):
    template_name = 'tasks/task_create.html'
    model = Task
    fields = ['name', 'description', 'status', 'type', 'project']

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.project.pk})

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        form.instance.project = project
        return super().form_valid(form)


class TaskUpdateView(TemplateView):
    template_name = "tasks/task_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = get_object_or_404(Task, pk=kwargs.get("pk"))
        form = TaskForm(
            initial={
                "name": task.name,
                "description": task.description,
                "status": task.status,
                "type": task.type.all(),
            }
        )
        context["form"] = form
        return context

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get("pk"))
        form = TaskForm(data=request.POST)
        if form.is_valid():
            types = form.cleaned_data.pop("type")
            task.name = form.cleaned_data.get("name")
            task.description = form.cleaned_data.get("description")
            task.status = form.cleaned_data.get("status")
            task.type.add(types)
            task.save()
            return redirect("task_view", pk=task.pk)
        else:
            return render(
                request,
                "tasks/task_update.html",
                {"status_choices": status_choices, "form": form},
            )


class TaskDeleteView(View):
    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get("pk"))
        return render(
            request,
            "tasks/task_delete.html",
            {
                "status_choices": status_choices,
                "type_choices": type_choices,
                "task": task,
            },
        )

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get("pk"))
        task.delete()
        return redirect("index")
