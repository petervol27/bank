# Generated by Django 5.1.2 on 2024-11-10 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Account",
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
                ("account_num", models.CharField(max_length=12, unique=True)),
                ("balance", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "branch",
                    models.IntegerField(
                        choices=[
                            (643, "Ha-Ganavim"),
                            (724, "Ha-Nochlim"),
                            (121, "Ha-Okchim"),
                            (400, "Ha-Gazlanim"),
                        ]
                    ),
                ),
                ("status", models.BooleanField()),
                ("created_date", models.DateField(auto_now_add=True)),
            ],
        ),
    ]
