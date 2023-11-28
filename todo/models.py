from django.db import models

status_choices = [('new', 'Новая'), ('in_progress', 'В процессе'),  ('done', 'Сделано')]


class Task(models.Model):
    name = models.TextField(max_length=3000, null=False, blank=False, verbose_name="Задача")
    status = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Статус', choices=status_choices)
    deadline = models.TextField(verbose_name='Сделать до', null=True)

    def __str__(self):
        return f'{self.id}. {self.task}'
