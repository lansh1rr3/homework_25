# Generated by Django 5.1.3 on 2024-12-05 14:13

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                        help_text="Введите название категории",
                        max_length=100,
                        verbose_name="Название категории",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="Введите описание категории",
                        null=True,
                        verbose_name="Описание категории",
                    ),
                ),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
            },
        ),
        migrations.RemoveField(
            model_name="dog",
            name="breed",
        ),
        migrations.CreateModel(
            name="Product",
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
                        help_text="Введите название продукта",
                        max_length=100,
                        verbose_name="Название продукта",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        help_text="Введите описание продукта",
                        verbose_name="Описание продукта",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузите фото продукта",
                        null=True,
                        upload_to="catalog/image",
                        verbose_name="Фото продукта",
                    ),
                ),
                (
                    "price",
                    models.IntegerField(
                        default=0,
                        validators=[django.core.validators.MaxValueValidator(10000)],
                        verbose_name="Цена за продукт",
                    ),
                ),
                (
                    "created_at",
                    models.DateField(
                        blank=True,
                        help_text="Введите дату создания",
                        null=True,
                        verbose_name="Дата создания",
                    ),
                ),
                (
                    "updated_at",
                    models.DateField(
                        blank=True,
                        help_text="Введите дату последнего изменения",
                        null=True,
                        verbose_name="Дата последнего изменения",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        help_text="Выберите категорию",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="catalog.category",
                        verbose_name="Категория",
                    ),
                ),
            ],
            options={
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
                "ordering": ["name", "category"],
            },
        ),
        migrations.DeleteModel(
            name="Breed",
        ),
        migrations.DeleteModel(
            name="Dog",
        ),
    ]
