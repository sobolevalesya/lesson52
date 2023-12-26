from django import forms
from django.forms import widgets
from todo.models import Type, Status


class TaskForm(forms.Form):
    name = forms.CharField(max_length=50, required=True, label="Задача")
    description = forms.CharField(
        max_length=3000, required=True, label="Описание", widget=widgets.Textarea
    )
    type = forms.ModelChoiceField(queryset=Type.objects.all(), label="Тип")
    status = forms.ModelChoiceField(queryset=Status.objects.all(), label="Статус")


class SimpleSearchForm(forms.Form):
    search = forms.CharField(required=False, label='Найти')


class ProjectForm(forms.Form):
    project_name = forms.CharField(max_length=50, required=True, label="Проект")
    project_description = forms.CharField(
        max_length=3000, required=True, label="Описание проекта", widget=widgets.Textarea
    )
    start_project = forms.DateField(label="Начало проекта")
    end_project = forms.DateField(label="Завершение проекта")


