from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course, Lesson


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Почта", help_text="Укажите почту", )
    phone = models.CharField(
        max_length=50,
        verbose_name="Телефон",
        help_text="Укажите номер телефона",
        blank=True,
        null=True,
    )
    avatar = models.ImageField(
        upload_to="users/image",
        blank=True,
        null=True,
        verbose_name="Фото",
        help_text="Загрузите фотографию",
    )
    country = models.CharField(
        max_length=50,
        verbose_name="Страна",
        help_text="Укажите страну",
        blank=True,
        null=True,
    )
    token = models.CharField(
        max_length=100, verbose_name="Тоken", null=True, blank=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email


class Payments(models.Model):
    CASH = "cash"
    NON_CASH = "non_cash"
    PAYMENT_OPTIONS = (
        (CASH, 'Наличный'),
        (NON_CASH, 'Безналичный')
    )
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='user'
    )
    payment_time = models.DateTimeField(
        verbose_name="Дата оплаты",
        help_text="Введите дату",
        auto_now_add=True,
        blank=True,
        null=True,
    )
    payment_course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="Оплаченный курс"
    )
    payment_lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="Оплаченный урок"
    )
    price = models.PositiveIntegerField(
        default=0,
        verbose_name="Стоимость покупки"
    )
    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_OPTIONS,
        default=CASH,
        verbose_name='Способ оплаты'
    )

    class Meta:
        verbose_name = "Оплата"
        verbose_name_plural = "Оплаты"

    def __str__(self):
        return self.payment_method
