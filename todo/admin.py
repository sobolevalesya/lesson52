from django.contrib import admin
from todo.models import Task, Status, TaskType, Type


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'status']


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'status_name']


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'type_name']


@admin.register(TaskType)
class TypeTaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'task', 'type']





