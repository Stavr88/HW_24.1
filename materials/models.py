from django.db import models


class Course(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование курса",
        help_text="Укажите название курса",
    )
    description = models.TextField(
        verbose_name="Описание курса",
        help_text="Опишите курс",
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to="materials/image",
        blank=True,
        null=True,
        verbose_name="Фото",
        help_text="Загрузите фото урока",
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название урока",
        help_text="Укажите название урока",
    )
    description = models.TextField(
        verbose_name="Описание урока",
        help_text="Опишите урок",
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to="materials/image",
        blank=True,
        null=True,
        verbose_name="Фото",
        help_text="Загрузите фото урока",
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='lesson_set'
    )
    video_url = models.URLField(
        verbose_name="Ссылка на урок",
        help_text="Video URL",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
        ordering = ["name"]

    def __str__(self):
        return f'{self.name}, {self.course}'
