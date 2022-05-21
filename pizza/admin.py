from django.contrib import admin

from .models import *


@admin.register(Product)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'ingredients', 'about', 'cat')


@admin.register(Price)
class PostAdmin(admin.ModelAdmin):
    list_display = ('product', 'description', 'price')


@admin.register(Category)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
