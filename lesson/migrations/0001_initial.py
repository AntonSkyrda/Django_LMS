# Generated by Django 5.1.6 on 2025-02-12 19:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("course", "0002_initial"),
        ("group", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Lesson",
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
                ("topic", models.CharField(max_length=255)),
                ("hour_count", models.PositiveIntegerField()),
                ("date", models.DateField()),
                ("time", models.TimeField()),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="lessons",
                        to="course.course",
                    ),
                ),
                (
                    "group",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="lessons",
                        to="group.group",
                    ),
                ),
            ],
        ),
    ]
