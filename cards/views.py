from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from decimal import Decimal
from .models import Card, CreditTransaction
from .serializers import CardSerializer, CreditTransactionSerializer
from accounts.models import Account


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_form_data(request):
    form_data = {
        "manufactorers": Card.MANUFACTURER_CHOICES,
        "payment_days": Card.PAYMENT_DATE_CHOICES,
    }
    return Response(form_data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def card_request(request):
    data = request.data
    account = Account.objects.get(user=request.user)
    card_limit = Card.objects.filter(account=account.id).count()
    if card_limit == 1:
        return Response({"failure": "sorry you already have a card"})
    else:
        data["account"] = account.id
        user = request.user
        data["owner_name"] = (
            user.first_name.capitalize() + " " + user.last_name.capitalize()
        )
        print(data)
        serializer = CardSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_card(request):
    user = request.user
    account = Account.objects.get(user=user)
    try:
        card = Card.objects.get(account=account.id)
        serializer = CardSerializer(card)
        return Response(serializer.data)
    except:
        return Response("")


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def card_history(request):
    user = request.user
    account = Account.objects.get(user=user)
    try:
        card = Card.objects.get(account=account.id)
        history = CreditTransaction.objects.filter(card=card.id)
        serializer = CreditTransactionSerializer(history, many=True)
        return Response(serializer.data)
    except:
        return Response("")


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def use_card(request):
    data = request.data
    user = request.user
    account = Account.objects.get(user=user)
    card = Card.objects.get(account=account.id)
    amount = data["amount"]
    card_limit = card.credit_limit
    new_credit_used = card.current_credit_used + Decimal(amount)
    if new_credit_used > card_limit:
        return Response({"failure": "you are over your card limit!"})
    else:
        data["card"] = card.id
        serializer = CreditTransactionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            card.current_credit_used = new_credit_used
            card.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
