from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None

    USERNAME_FIELD = 'email'
    avatar = models.ImageField(upload_to="media/")
    email = models.EmailField(unique=True, verbose_name='Почта', null=False, blank=False)
    phone = models.CharField(max_length=11, verbose_name='телефон', null=True, blank=True)
    city = models.CharField(max_length=30, verbose_name='город', null=True, blank=True)
    token = models.CharField(max_length=255, verbose_name="Токен", blank=True, null=True)

    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return self.email
