from django.db import models
from bank import settings
from accounts.models import Account


class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ("salary", "Salary"),
        ("transfer", "Transfer"),
        ("payment", "Payment"),
        ("withdraw", "Withdraw"),
        ("deposit", "Deposit"),
        ("loan", "Loan"),
        ("credit", "Credit"),
        ("credit_usage", "Pay With Card"),
    ]

    date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    sender_account = models.ForeignKey(
        Account,
        related_name="sent_transactions",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    reciever_account = models.ForeignKey(
        Account,
        related_name="received_transactions",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPES)
    sender_new_balance = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    reciever_new_balance = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    details = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.transaction_type.capitalize()} -{self.sender_account} to {self.reciever_account}- {self.amount} on {self.date}"
