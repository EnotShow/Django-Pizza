from django.db import models
from django.urls import reverse

from users.models import User
from pizza.models import Product


class Checkout(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    order = models.CharField(max_length=9999)
    status = models.BooleanField(default=True)
