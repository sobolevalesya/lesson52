from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils.http import urlencode
from django.db.models import Q
from todo.models import Task, status_choices, TaskType, Status, Type, type_choices
from todo.forms import TaskForm, SimpleSearchForm
from django.views.generic import View, TemplateView, FormView, ListView, DetailView


class IndexView(ListView):
    model = Task
    template_name = 'tasks/index.html'
    context_object_name = 'tasks'
    paginate_by = 5
    paginate_orphans = 3
    ordering = ('-created_at',)

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_value(self):
        if self.search_form.is_valid():
            return self.search_form.cleaned_data['search']
        return None

    def dispatch(self, request, *args, **kwargs):
        self.search_form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            queryset = queryset.filter(Q(name__icontains=self.search_value) |
                                       Q(description__icontains=self.search_value))
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.search_form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
            context['search_value'] = self.search_value
        return context


class TaskView(DetailView):
    model = Task
    template_name = "tasks/task_view.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['comments'] = self.object.comments.order_by('-created_at')
    #     return context

def task_view(request, *args, pk, **kwargs):
    task = get_object_or_404(Task, pk=pk)
    return render(request, "tasks/task_view.html", {"task": task})


class TaskCreateView(FormView):
    template_name = 'tasks/task_create.html'
    form_class = TaskForm

    def form_valid(self, form):
        self.task = form.save()
        return redirect('task_view', pk=self.task.pk)


class TaskUpdateView(FormView):
    template_name = 'tasks/task_update.html'
    form_class = TaskForm

    def dispatch(self, request, *args, **kwargs):
        self.task = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(Task, pk=self.kwargs.get('pk'))

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.task
        return kwargs

    def form_valid(self, form):
        form.save()
        return redirect("task_view", pk=self.task.pk)


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
