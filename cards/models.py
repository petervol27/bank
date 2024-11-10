from django.db import models
from django.utils import timezone
import random
from accounts.models import Account


class Card(models.Model):
    MANUFACTURER_CHOICES = [
        ("vasa", "4580"),
        ("mustercard", "5326"),
        ("italian_express", "4675"),
    ]
    PAYMENT_DATE_CHOICES = [
        (10, "10"),
        (1, "1"),
    ]

    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    owner_name = models.CharField(max_length=100)
    credit_limit = models.IntegerField()
    payment_date = models.IntegerField(choices=PAYMENT_DATE_CHOICES, default=10)
    manufacturer = models.CharField(max_length=20, choices=MANUFACTURER_CHOICES)
    card_number = models.CharField(max_length=19, unique=True, blank=True)
    cvv = models.CharField(max_length=3, blank=True)
    expiration_date = models.CharField(max_length=5, blank=True)
    current_credit_used = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.card_number:
            self.generate_unique_card_number()

        if not self.cvv:
            self.cvv = f"{random.randint(100, 999)}"

        if not self.expiration_date:
            expiration_year = timezone.now().year + 4
            expiration_month = timezone.now().month
            self.expiration_date = f"{expiration_month}/{str(expiration_year)[-2:]}"

        super().save(*args, **kwargs)

    def generate_unique_card_number(self):
        prefix = dict(self.MANUFACTURER_CHOICES).get(self.manufacturer, "0000")

        while True:
            random_digits = "".join([str(random.randint(0, 9)) for _ in range(12)])
            generated_card_number = (
                f"{prefix}-{random_digits[:4]}-{random_digits[4:8]}-{random_digits[8:]}"
            )

            if not Card.objects.filter(card_number=generated_card_number).exists():
                self.card_number = generated_card_number
                break

    def __str__(self):
        return f"{self.manufacturer.capitalize()} - {self.card_number}"


class CreditTransaction(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    amount = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    details = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.details} on {self.date} by {self.card}"
