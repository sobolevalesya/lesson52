from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from todo.models import Task, status_choices, TaskType, Status, Type, type_choices
from todo.forms import TaskForm
from django.views.generic import View, TemplateView, FormView


class IndexView(View):
    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all()
        return render(request, "index.html", {"tasks": tasks})


class TaskView(TemplateView):
    template_name = "task_view.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["task"] = get_object_or_404(Task, pk=kwargs.get("pk"))
        return context


def task_view(request, *args, pk, **kwargs):
    task = get_object_or_404(Task, pk=pk)
    return render(request, "task_view.html", {"task": task})


class TaskCreateView(FormView):
    template_name = 'task_create.html'
    form_class = TaskForm
    # success_url = reverse_lazy('index')

    # def get_success_url(self):
    #     return reverse('task_view', kwargs={'pk': self.task.pk})

    def form_valid(self, form):
        # form = TaskForm(data=self.request.POST)
        types = form.cleaned_data.pop('type')
        self.task = Task.objects.create(
            name=form.cleaned_data.get("name"),
            description=form.cleaned_data.get("description"),
            status=form.cleaned_data.get("status"),
        )
        print(types)
        self.task.type.set(types)
        return redirect('task_view', pk=self.task.pk)


class TaskUpdateView(FormView):
    template_name = 'task_update.html'
    form_class = TaskForm

    def dispatch(self, request, *args, **kwargs):
        self.task = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(Task, pk=self.kwargs.get('pk'))

    def get_initial(self):
        initial = {
            "name": self.task.name,
            "description": self.task.description,
            "status": self.task.status,
            "type": self.task.type.all(),
        }
        return initial

    def form_valid(self, form):
        types = form.cleaned_data.pop("type")
        self.task.name = form.cleaned_data.get("name")
        self.task.description = form.cleaned_data.get("description")
        self.task.status = form.cleaned_data.get("status")
        self.task.type.add(types)
        self.task.save()
        return redirect("task_view", pk=self.task.pk)


class TaskDeleteView(View):
    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get("pk"))
        return render(
            request,
            "task_delete.html",
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
