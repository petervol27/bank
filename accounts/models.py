from django.db import models
from bank import settings
from datetime import timedelta


class Account(models.Model):
    BRANCH_CHOICES = [
        (643, "Ha-Ganavim"),
        (724, "Ha-Nochlim"),
        (121, "Ha-Okchim"),
        (400, "Ha-Gazlanim"),
    ]

    account_num = models.CharField(unique=True, max_length=12)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    branch = models.IntegerField(choices=BRANCH_CHOICES)
    status = models.BooleanField()
    created_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.account_num
