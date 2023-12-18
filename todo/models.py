from django.db import models
from django.core.validators import MinLengthValidator

status_choices = [("new", "Новая"), ("in_progress", "В процессе"), ("done", "Сделано")]
type_choices = [("task", "Задача"), ("bug", "Ошибка"), ("enhancement", "Улучшение")]


class AbstractModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Время изменения")

    class Meta:
        abstract = True


# class TypeTask(AbstractModel):
#     name = models.TextField(max_length=3000, verbose_name="Задача", unique=True)
#     descript = models.TextField(max_length=400, null=True, blank=True, verbose_name='Описание')
#
#     def __str__(self):
#         return f'{self.id}. {self.name}'


class Task(AbstractModel):
    name = models.CharField(
        max_length=50, null=False, blank=False, validators=[MinLengthValidator(4)], verbose_name="Задача"
    )
    description = models.TextField(
        max_length=3000, null=True, blank=False, verbose_name="Описание"
    )
    status = models.ForeignKey(
        "todo.Status",
        on_delete=models.RESTRICT,
        verbose_name="Статус",
        related_name="tasks",
        blank=True,
    )
    type = models.ManyToManyField(
        "todo.Type",
        through="todo.TaskType",
        through_fields=("task", "type"),
        verbose_name="Тип",
        related_name="tasks",
        blank=True,
    )

    def __str__(self):
        return f"{self.id}. {self.name}"


class Status(AbstractModel):
    status_name = models.CharField(
        max_length=31, choices=status_choices, verbose_name="Статус"
    )

    def __str__(self):
        return self.status_name


class Type(AbstractModel):
    type_name = models.CharField(
        max_length=31, choices=type_choices, verbose_name="Тип"
    )

    def __str__(self):
        return self.type_name


class TaskType(models.Model):
    task = models.ForeignKey(
        "todo.Task",
        related_name="task_type",
        on_delete=models.CASCADE,
        verbose_name="Задача",
    )
    type = models.ForeignKey(
        "todo.Type",
        related_name="type_task",
        verbose_name="Тип",
        on_delete=models.RESTRICT,
    )

    def __str__(self):
        return "{} | {}".format(self.task, self.type)
