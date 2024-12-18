# Generated by Django 5.1.2 on 2024-11-10 20:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Card",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("owner_name", models.CharField(max_length=100)),
                ("credit_limit", models.IntegerField()),
                (
                    "payment_date",
                    models.IntegerField(choices=[(10, "10"), (1, "1")], default=10),
                ),
                (
                    "manufacturer",
                    models.CharField(
                        choices=[
                            ("vasa", "4580"),
                            ("mustercard", "5326"),
                            ("italian_express", "4675"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "card_number",
                    models.CharField(blank=True, max_length=19, unique=True),
                ),
                ("cvv", models.CharField(blank=True, max_length=3)),
                ("expiration_date", models.CharField(blank=True, max_length=5)),
                ("current_credit_used", models.IntegerField(default=0)),
                (
                    "account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.account",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CreditTransaction",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("amount", models.IntegerField()),
                ("date", models.DateTimeField(auto_now_add=True)),
                ("details", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "card",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="cards.card"
                    ),
                ),
            ],
        ),
    ]
