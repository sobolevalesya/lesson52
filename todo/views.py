from django.shortcuts import render, reverse, redirect, get_object_or_404
from todo.models import Task, status_choices, TypeTask
from django.http import HttpResponseRedirect, Http404


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
        return render(request, 'task_create.html', {'status_choices': status_choices, 'types_task': types_task})
    elif request.method == "POST":
        task = Task.objects.create(
            name=request.POST.get('task'),
            description=request.POST.get('description'),
            status=request.POST.get('status'),
            deadline=request.POST.get('deadline'),
            type_id=request.POST.get('type_id')
        )
        return redirect('index')


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
        task.save()
        return redirect('index')


def task_delete_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "GET":
        types_task = TypeTask.objects.all()
        return render(request, 'task_delete.html', {'status_choices': status_choices, 'types_task': types_task, 'task': task})
    elif request.method == "POST":
        task.delete()
        return redirect('index')