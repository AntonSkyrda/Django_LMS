# Generated by Django 5.1.6 on 2025-02-12 19:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("assignments", "0002_initial"),
        ("group", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="teachingassignment",
            name="group",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="assignments",
                to="group.group",
            ),
        ),
    ]
