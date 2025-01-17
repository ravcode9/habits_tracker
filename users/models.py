from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    phone = models.CharField(max_length=35, verbose_name='телефон',
                             blank=True, null=True)
    avatar = models.ImageField(upload_to='users/avatars/',
                               verbose_name='аватар',
                               blank=True, null=True)
    town = models.CharField(max_length=100, blank=True, null=True)
    token = models.CharField(max_length=100, verbose_name="Токен",
                             blank=True, null=True)
    is_active = models.BooleanField(default='True', verbose_name='активность')
    chat_id = models.CharField(max_length=50,
                               verbose_name="айди чата Телеграмм",
                               help_text="Укажите айди чата Телеграмм",
                               blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = "Пользователи"
        ordering = ['email']
