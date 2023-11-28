from django.shortcuts import render
from todo.models import Task, status_choices
from django.http import HttpResponseRedirect


def index_view(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks': tasks})


def task_view(request):
    task_id = request.GET.get('id')
    task = Task.objects.get(id=task_id)
    return render(request, 'task_view.html', {'task': task})


def task_create_view(request):
    if request.method == "GET":
        return render(request, 'task_create.html', {'status_choices': status_choices})
    elif request.method == "POST":
        Task.objects.create(
            name=request.POST.get('task'),
            status=request.POST.get('status'),
            deadline=request.POST.get('deadline')
        )
        return HttpResponseRedirect('/')
