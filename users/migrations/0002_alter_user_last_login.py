# Generated by Django 4.2.2 on 2024-11-18 18:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="last_login",
            field=models.DateTimeField(
                blank=True,
                default=datetime.datetime.now,
                null=True,
                verbose_name="Время последнего посещения",
            ),
        ),
    ]
