from django.db import models
from django.urls import reverse


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(upload_to='', blank=True, verbose_name='Фото')
    ingredients = models.CharField(max_length=500, blank=True, verbose_name='Ингридиенты')
    about = models.CharField(max_length=500, verbose_name='Описание')
    cat = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')

    class Meta:
        verbose_name = 'Товары'
        verbose_name_plural = 'Товары'
        ordering = ['pk']

    def get_absolute_url(self):
        return reverse('product', kwargs={'product_id': self.pk})

    def __str__(self):
        return str(self.title)


class Price(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='Товар')
    description = models.CharField(max_length=255, verbose_name='Подпись')
    price = models.IntegerField(null=True, verbose_name='Цена')

    class Meta:
        verbose_name = 'Цены'
        verbose_name_plural = 'Цены'
        ordering = ['pk']

    def get_absolute_url(self):
        return reverse('item', kwargs={'item_id': self.pk})

    def __str__(self):
        return str(self.product)


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(unique=True, verbose_name='Слаг')

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'
        ordering = ['pk']

    def get_absolute_url(self):
        return reverse('cat', kwargs={'cat_slug': self.slug})

    def __str__(self):
        return str(self.title)
