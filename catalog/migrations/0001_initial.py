# Generated by Django 5.1.3 on 2024-12-05 11:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Breed",
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
                    "name",
                    models.CharField(
                        help_text="Введите название породы собаки",
                        max_length=100,
                        verbose_name="Название породы",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="Введите описание породы собаки",
                        null=True,
                        verbose_name="Описание породы",
                    ),
                ),
            ],
            options={
                "verbose_name": "Собака",
                "verbose_name_plural": "Собаки",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Dog",
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
                    "name",
                    models.CharField(
                        help_text="Введите кличку собаки",
                        max_length=100,
                        verbose_name="Кличка",
                    ),
                ),
                (
                    "photo",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузите фото собаки",
                        null=True,
                        upload_to="catalog/photo",
                        verbose_name="Фото",
                    ),
                ),
                (
                    "date_born",
                    models.DateField(
                        blank=True,
                        help_text="Укажите дату рождения",
                        null=True,
                        verbose_name="Дата рождения",
                    ),
                ),
                (
                    "breed",
                    models.ForeignKey(
                        blank=True,
                        help_text="Введите породу собаки",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="catalog",
                        to="catalog.breed",
                        verbose_name="Порода",
                    ),
                ),
            ],
            options={
                "verbose_name": "Собака",
                "verbose_name_plural": "Собаки",
                "ordering": ["name", "breed"],
            },
        ),
    ]
