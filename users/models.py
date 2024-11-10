from django.db import models
from django.contrib.auth.models import AbstractUser


class BankUser(AbstractUser):
    phone = models.CharField(max_length=12)
    citizen_num = models.CharField(max_length=9, unique=True)
    address = models.CharField(max_length=150)

    def __str__(self):
        return self.username
