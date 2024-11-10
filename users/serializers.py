from .models import BankUser
from rest_framework import serializers


class BankUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankUser
        fields = "__all__"
