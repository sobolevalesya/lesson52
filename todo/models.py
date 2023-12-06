from django.db import models

status_choices = [('new', 'Новая'), ('in_progress', 'В процессе'),  ('done', 'Сделано')]


class TypeTask(models.Model):
    name = models.TextField(max_length=3000, verbose_name="Задача", unique=True)
    descript = models.TextField(max_length=400, null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return f'{self.id}. {self.name}'


class Task(models.Model):
    name = models.TextField(max_length=50, null=False, blank=False, verbose_name="Задача")
    description = models.TextField(max_length=3000, null=True, blank=False, verbose_name="Описание")
    status = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Статус', choices=status_choices)
    deadline = models.TextField(verbose_name='Сделать до', null=True)
    type = models.ForeignKey('todo.TypeTask', on_delete=models.RESTRICT, verbose_name='Тип', related_name='tasks', null=True)

    def __str__(self):
        return f'{self.id}. {self.name}'
