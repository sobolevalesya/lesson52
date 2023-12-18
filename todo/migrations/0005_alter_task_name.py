# Generated by Django 4.2.7 on 2023-12-18 23:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("todo", "0004_alter_tasktype_task"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="name",
            field=models.CharField(
                max_length=50,
                validators=[django.core.validators.MinLengthValidator(4)],
                verbose_name="Задача",
            ),
        ),
    ]
