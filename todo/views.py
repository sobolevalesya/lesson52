from django.shortcuts import render, reverse, redirect, get_object_or_404
from todo.models import Task, status_choices, TypeTask
from todo.validate_char_field import task_validate

def index_view(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks': tasks})


def task_view(request, *args, pk, **kwargs):
    # task_id = request.GET.get('id')
    # task = Task.objects.get(id=task_id)
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task_view.html', {'task': task})


def task_create_view(request):
    if request.method == "GET":
        types_task = TypeTask.objects.all()
        return render(request, 'task_create.html', {'status_choices': status_choices})
    elif request.method == "POST":
        name = request.POST.get('task')
        description = request.POST.get('description')
        status = request.POST.get('status')
        deadline = request.POST.get('deadline')
        task = Task(name=name, description=description, status=status, deadline=deadline)
        errors = task_validate(name, description, status, deadline)

        if errors:
            return render(request, 'task_create.html', {'status_choices': status_choices, 'errors': errors, 'task': task})
        else:
            task.save()
            return redirect('task_view', pk=task.pk)


def task_update_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "GET":
        types_task = TypeTask.objects.all()
        return render(request, 'task_update.html', {'status_choices': status_choices, 'types_task': types_task, 'task': task})
    elif request.method == "POST":

        task.name = request.POST.get('task')
        task.description = request.POST.get('description')
        task.status = request.POST.get('status')
        task.deadline = request.POST.get('deadline')
        task.type_id = request.POST.get('type_id')
        errors = task_validate(task.name, task.description, task.status, task.deadline)

        if errors:
            return render(request, 'task_update.html',
                          {'status_choices': status_choices, 'errors': errors, 'task': task})
        else:
            task.save()
            return redirect('task_view', pk=task.pk)


def task_delete_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "GET":
        types_task = TypeTask.objects.all()
        return render(request, 'task_delete.html', {'status_choices': status_choices, 'types_task': types_task, 'task': task})
    elif request.method == "POST":
        task.delete()
        return redirect('index')