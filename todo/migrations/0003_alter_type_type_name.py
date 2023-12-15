# Generated by Django 4.2.7 on 2023-12-14 09:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("todo", "0002_alter_status_status_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="type",
            name="type_name",
            field=models.CharField(
                choices=[
                    ("task", "Задача"),
                    ("bug", "Ошибка"),
                    ("enhancement", "Улучшение"),
                ],
                max_length=31,
                verbose_name="Тип",
            ),
        ),
    ]
