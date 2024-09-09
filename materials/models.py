from django.db import models


NULLABLE = {"blank": True, "null": True}


class Course(models.Model):

    name = models.CharField(max_length=64, verbose_name='название курса')
    preview = models.ImageField(upload_to='media/', **NULLABLE,verbose_name='превью курса')
    description = models.TextField(max_length=1024, verbose_name='описание курса')

    class Meta:
        verbose_name = "курс"
        verbose_name_plural = "курсы"

class Lesson(models.Model):
    name = models.CharField(max_length=64, verbose_name='название урока')
    description = models.TextField(max_length=1024, verbose_name='описание урока')
    preview = models.ImageField(upload_to='media/', verbose_name='превью урока')
    video_url = models.URLField(**NULLABLE, verbose_name='ссылка на видео')
    course = models.ForeignKey(Course,on_delete=models.CASCADE, **NULLABLE , verbose_name='курс к которому относится урок')

    class Meta:
        verbose_name = "урок"
        verbose_name_plural = "уроки"