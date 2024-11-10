from django.contrib import admin
from .models import BankUser
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    model = BankUser

    fieldsets = UserAdmin.fieldsets + (
        (
            "Additional Info",
            {
                "fields": ("address", "citizen_num", "phone"),
            },
        ),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "password1",
                    "password2",
                    "address",
                    "citizen_num",
                    "phone",
                ),
            },
        ),
    )

    list_display = ["username", "first_name", "last_name"]


admin.site.register(BankUser, CustomUserAdmin)
