from rest_framework import serializers
from .models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    formatted_date = serializers.SerializerMethodField()

    class Meta:
        model = Transaction
        fields = "__all__"

    def get_formatted_date(self, obj):
        return obj.date.strftime("%B %d, %Y, %I:%M %p")
