from django.shortcuts import render, reverse, redirect, get_object_or_404
from todo.models import Task, status_choices, TaskType, Status, Type
from todo.forms import TaskForm
from django.views.generic import View, TemplateView


class IndexView(View):
    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all()
        return render(request, 'index.html', {'tasks': tasks})


class TaskView(TemplateView):
    template_name = 'task_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=kwargs.get('pk'))
        return context



def task_view(request, *args, pk, **kwargs):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task_view.html', {'task': task})


def task_create_view(request):
    if request.method == "GET":
        form = TaskForm()
        return render(request, 'task_create.html', {'status_choices': status_choices, 'form': form})
    elif request.method == "POST":
        form = TaskForm(data=request.POST)

        if form.is_valid():
            task = Task.objects.create(
                name=form.cleaned_data.get('name'),
                description=form.cleaned_data.get('description'),
                status=form.cleaned_data.get('status')

            )
            task.type.add(form.cleaned_data.get('type'))
            return redirect('task_view', pk=task.pk)
        else:
            return render(request, 'task_create.html', {'status_choices': status_choices, 'form': form})



def task_update_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "GET":
        form = TaskForm(initial={
            'name': task.name,
            'description': task.description,
            'status': task.status,
            'type': task.type.first()
        })
        return render(request, 'task_update.html', {'status_choices': status_choices, 'form': form})
    elif request.method == "POST":

        form = TaskForm(data=request.POST)
        if form.is_valid():
            task.name = form.cleaned_data.get('name')
            task.description = form.cleaned_data.get('description')
            task.status = form.cleaned_data.get('status')
            task.save()
            return redirect('task_view', pk=task.pk)
        else:
            return render(request, 'task_update.html',
                      {'status_choices': status_choices, 'form': form})


def task_delete_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "GET":
        types_task = TaskType.objects.all()
        return render(request, 'task_delete.html', {'status_choices': status_choices, 'types_task': types_task, 'task': task})
    elif request.method == "POST":
        task.delete()
        return redirect('index')