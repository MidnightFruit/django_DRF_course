from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import NULLABLE, Course, Lesson


class User(AbstractUser):
    username = None

    USERNAME_FIELD = 'email'
    avatar = models.ImageField(upload_to="media/", **NULLABLE,verbose_name='аватар пользователя')
    email = models.EmailField(unique=True, verbose_name='почта', null=False, blank=False)
    phone = models.CharField(max_length=11, verbose_name='телефон', null=True, blank=True)
    city = models.CharField(max_length=30, verbose_name='город', null=True, blank=True)

    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return self.email


class Payment(models.Model):

    METHOD = [
        ('наличные', 'Наличная оплата'),
        ('перевод', 'Перевод на счет'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    payment_date = models.DateField(**NULLABLE, verbose_name='дата оплаты')
    course = models.ForeignKey(Course, **NULLABLE, on_delete=models.CASCADE, verbose_name='оплаченный курс')
    lesson = models.ForeignKey(Lesson, **NULLABLE, on_delete=models.CASCADE, verbose_name='оплаченный урок')
    value = models.PositiveIntegerField(verbose_name='сумма оплаты')
    method = models.CharField(verbose_name='метод оплаты', choices=METHOD)

    class Meta:
        verbose_name = 'платёж'
        verbose_name_plural = 'платежи'
