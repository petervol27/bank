from django.db import models
from bank import settings
from datetime import timedelta


class Account(models.Model):
    account_num = models.CharField(unique=True, max_length=12)
    balance = models.IntegerField()
    branch = models.IntegerField()
    status = models.BooleanField()
    created_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.account_num
