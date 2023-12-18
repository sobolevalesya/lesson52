from django import forms
from django.forms import widgets
from todo.models import Type, Status, Task
from django.core.validators import BaseValidator
from django.utils.deconstruct import deconstructible
from django.core.validators import MinLengthValidator

#
# @deconstructible
# class MinLengthValidator(BaseValidator):
#     message = 'Value "%(value)s" has length of %(show_value)d! It should be at least %(limit_value)d symbols long!'
#     code = 'too_short'
#
#     def compare(self, a, b):
#         return a < b
#
#     def clean(self, x):
#         return len(x)
#
#
# def at_least_5(value):
#     if len(value) < 5:
#         raise forms.ValidationError('Название не может быть короче 5 символов')


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
        # exclude = ()
        widgets = {'type': forms.CheckboxSelectMultiple}
        error_messages = {
            'name': {
                'required': 'Please enter',
                'min_length': 'Название не может быть короче 4 символов'
                    }
        }

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')
        if name == description:
            raise forms.ValidationError('Название и описание задачи не могут быть одинаковыми')
        return cleaned_data

    # def clean_name(self):
    #     name = self.cleaned_data['name']
    #     if len(name) < 5:
    #         raise forms.ValidationError('Название слишком короткое')
    #
    #     return name
