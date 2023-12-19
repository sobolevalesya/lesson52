from django import forms
from django.forms import widgets
from todo.models import Type, Status, Task
from django.core.validators import BaseValidator
from django.utils.deconstruct import deconstructible
from django.core.validators import MinLengthValidator, MaxLengthValidator


class TaskForm(forms.ModelForm):
    # name = forms.CharField(max_length=50, required=True, validators=[MinLengthValidator(4, message='Название слишком короткое')], label="Задача")
    # description = forms.CharField(
    #     max_length=3000, required=True, label="Описание", widget=widgets.Textarea
    # )
    # type = forms.ModelChoiceField(queryset=Type.objects.all(), label="Тип")
    # status = forms.ModelChoiceField(queryset=Status.objects.all(), label="Статус")
    class Meta:
        model = Task
        fields = ('name', 'description', 'status', 'type')
        widgets = {'type': forms.CheckboxSelectMultiple}
        error_messages = {
            'name': {
                'required': 'Please enter',
                'min_length': 'Название не может быть короче 4 символов',
                    },
                'description': {
                    'required': 'Please enter',
                    'max_length': 'Описание не может быть длиннее 300 символов'
                }
        }

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')
        if name == description:
            raise forms.ValidationError('Название и описание задачи не могут быть одинаковыми')
        return cleaned_data