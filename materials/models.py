from django.db import models

from config.settings import AUTH_USER_MODEL


NULLABLE = {"blank": True, "null": True}


class Course(models.Model):

    name = models.CharField(max_length=64, verbose_name='название курса')
    preview = models.ImageField(upload_to='media/', **NULLABLE,verbose_name='превью курса')
    description = models.TextField(max_length=1024, verbose_name='описание курса')
    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='создатель курса')

    class Meta:
        verbose_name = "курс"
        verbose_name_plural = "курсы"


class Lesson(models.Model):
    name = models.CharField(max_length=64, verbose_name='название урока')
    description = models.TextField(max_length=1024, verbose_name='описание урока')
    preview = models.ImageField(upload_to='media/', **NULLABLE, verbose_name='превью урока')
    video_url = models.URLField(**NULLABLE, verbose_name='ссылка на видео')
    course = models.ForeignKey(Course,on_delete=models.CASCADE, **NULLABLE , verbose_name='курс к которому относится урок')
    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='создатель урока')

    class Meta:
        verbose_name = "урок"
        verbose_name_plural = "уроки"


class Subscribe(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='пользователь')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс')

    class Meta:
        verbose_name = "подписка"
        verbose_name_plural = "подписки"

    # def __str__(self):
    #     return f"{self.user.name} {self.course.name}"
