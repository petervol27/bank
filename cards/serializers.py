from rest_framework import serializers
from .models import Card, CreditTransaction


class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = "__all__"


class CreditTransactionSerializer(serializers.ModelSerializer):
    formatted_date = serializers.SerializerMethodField()

    class Meta:
        model = CreditTransaction
        fields = "__all__"

    def get_formatted_date(self, obj):
        return obj.date.strftime("%B %d, %Y, %I:%M %p")
