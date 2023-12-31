# Generated by Django 4.2.7 on 2023-12-24 06:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("todo", "0003_alter_type_type_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "project_name",
                    models.CharField(max_length=50, verbose_name="Проект"),
                ),
                (
                    "project_description",
                    models.TextField(
                        max_length=3000, null=True, verbose_name="Описание проекта"
                    ),
                ),
                ("start_project", models.DateField(verbose_name="Начало проекта")),
                (
                    "end_project",
                    models.DateField(
                        blank=True, null=True, verbose_name="Завершение проекта"
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="tasktype",
            name="task",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="task_type",
                to="todo.task",
                verbose_name="Задача",
            ),
        ),
    ]
