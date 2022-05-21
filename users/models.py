from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=255, unique=False, blank=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True)
