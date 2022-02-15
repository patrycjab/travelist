from django.contrib.auth.models import AbstractUser
from django.db import models

from account.managers import CustomUserManager


class CustomUser(AbstractUser):
    balance = models.FloatField(default=0)
    referrer_email = models.EmailField(blank=True, null=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=256, unique=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


class SourcePoints(models.Model):
    name = models.CharField(max_length=256, unique=True)


class Transaction(models.Model):
    source_type = models.ForeignKey(SourcePoints, on_delete=models.CASCADE)
    value = models.FloatField()
    account = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
