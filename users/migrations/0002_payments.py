# Generated by Django 4.2.2 on 2024-10-24 11:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0001_initial"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Payments",
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
                    "payment_time",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="Введите дату",
                        null=True,
                        verbose_name="Дата оплаты",
                    ),
                ),
                (
                    "cost",
                    models.PositiveIntegerField(
                        default=0, verbose_name="Стоимость покупки"
                    ),
                ),
                (
                    "payment_method",
                    models.CharField(
                        choices=[("cash", "Наличный"), ("non_cash", "Безналичный")],
                        default="cash",
                        max_length=20,
                        verbose_name="Способ оплаты",
                    ),
                ),
                (
                    "payment_course",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="materials.course",
                        verbose_name="Оплаченный курс",
                    ),
                ),
                (
                    "payment_lesson",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="materials.lesson",
                        verbose_name="Оплаченный урок",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Оплата",
                "verbose_name_plural": "Оплаты",
            },
        ),
    ]
