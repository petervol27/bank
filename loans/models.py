from django.db import models
from accounts.models import Account


class Loan(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    date_taken = models.DateField(null=True)
    date_finished = models.DateField(null=True)
    amount = models.IntegerField()
    payments = models.IntegerField()
    loan_number = models.IntegerField(null=True, blank=True)
    left_to_pay = models.IntegerField(null=True)

    def __str__(self):
        return f"Loan for {self.account} on {self.date_taken} "
