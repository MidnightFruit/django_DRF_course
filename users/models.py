from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import NULLABLE


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
