from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import reverse, render, redirect, get_object_or_404
from todo.models import Project
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from todo.forms import TaskForm, SimpleSearchForm, ProjectForm
from django.utils.http import urlencode
from django.db.models import Q


class IndexView(ListView):
    model = Project
    template_name = 'projects/index.html'
    context_object_name = 'projects'
    paginate_by = 5
    paginate_orphans = 0
    ordering = ('project_name',)

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_value(self):
        if self.search_form.is_valid():
            return self.search_form.cleaned_data['search']
        return None

    def dispatch(self, request, *args, **kwargs):
        print(request.user)
        self.search_form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            queryset = queryset.filter(Q(project_name__icontains=self.search_value) |
                                       Q(project_description__icontains=self.search_value))
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.search_form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
            context['search_value'] = self.search_value
        return context


class ProjectView(DetailView):
    model = Project
    template_name = "projects/project_view.html"


def project_view(request, *args, pk, **kwargs):
    project = get_object_or_404(Project, pk=pk)
    return render(request, "projects/project_view.html", {"project": project})


class ProjectUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = "projects/project_update.html"
    model = Project
    form_class = ProjectForm
    permission_required = 'todo.change_project'

    def has_permission(self):
        return super().has_permission() or self.request.user == self.get_object().users


class ProjectDeleteView(PermissionRequiredMixin, DeleteView):
    model = Project
    success_url = '/'
    template_name = "projects/project_delete.html"

    def has_permission(self):
        return self.request.user.has_perm('todo.delete_project') or self.request.user == self.get_object().users


class ProjectCreateView(LoginRequiredMixin, CreateView):
    template_name = 'projects/project_create.html'
    model = Project
    fields = ['project_name', 'project_description', 'start_project', 'end_project', 'users']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.users = self.request.user
        self.object.save()
        form.save_m2m()
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('todo:project_view', kwargs={'pk': self.object.pk})

