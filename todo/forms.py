from django import forms
from todo.models import Task


class TaskForm(forms.ModelForm):
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


class SimpleSearchForm(forms.Form):
    search = forms.CharField(required=False, label='Найти')
