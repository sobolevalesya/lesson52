from django import forms
from django.forms import widgets
from todo.models import status_choices


class TaskForm(forms.Form):
    name = forms.CharField(max_length=50, required=True, label='Задача')
    description = forms.CharField(max_length=3000, required=True, label='Описание', widget=widgets.Textarea)
    status = forms.ChoiceField(required=True, label='Статус', widget=widgets.Select, choices=status_choices)
    deadline = forms.CharField(required=True, label='Сделать до')


