from django.db import models
from django.urls import reverse

from users.models import User
from pizza.models import Product


class CartItem(models.Model):
    count = models.IntegerField(),
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')

    def get_absolute_url(self):
        return reverse('item', kwargs={'item_id': self.pk})

    def __str__(self):
        return str(self.product)


class Cart(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Владелец корзины'
    )
    item = models.ForeignKey(
        CartItem,
        on_delete=models.CASCADE,
        verbose_name='Предмет'
    )

    def get_absolute_url(self):
        return reverse('cart', kwargs={'cart_id': self.pk})

    def __str__(self):
        return str(self.owner)


