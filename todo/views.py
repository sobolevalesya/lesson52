from django.shortcuts import render, reverse, redirect, get_object_or_404
from todo.models import Task, status_choices
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
        return render(request, 'task_create.html', {'status_choices': status_choices})
    elif request.method == "POST":
        task = Task.objects.create(
            name=request.POST.get('task'),
            description=request.POST.get('description'),
            status=request.POST.get('status'),
            deadline=request.POST.get('deadline')
        )
        return redirect('index')
