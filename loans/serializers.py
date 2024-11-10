from rest_framework import serializers
from .models import Loan
from dateutil.relativedelta import relativedelta
from datetime import date


class LoanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Loan
        fields = "__all__"

    def create(self, validated_data):
        validated_data["date_taken"] = date.today()

        payments = validated_data.get("payments")
        if payments:
            validated_data["date_finished"] = validated_data[
                "date_taken"
            ] + relativedelta(months=payments)

        return super().create(validated_data)
