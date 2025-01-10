from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Transaction
from .serializers import TransactionSerializer
from accounts.models import Account
from loans.models import Loan
from cards.models import Card
from decimal import Decimal
from django.db.models import Q


@permission_classes([IsAuthenticated])
@api_view(["GET"])
def transaction_types(request):
    types = Transaction.TRANSACTION_TYPES
    return Response(types)


@permission_classes([IsAuthenticated])
@api_view(["POST"])
def makeTransaction(request):
    data = request.data
    transaction = data.get("transaction_type")
    amount = data.get("amount")
    reciever_id = data.get("reciever_account")
    sender_id = data.get("sender_account")
    reciever = Account.objects.get(id=reciever_id) if reciever_id else None
    sender = Account.objects.get(id=sender_id) if sender_id else None
    if transaction == "salary":
        new_balance = reciever.balance + Decimal(amount)
        data["reciever_new_balance"] = new_balance
        reciever.balance = new_balance
        reciever.save()
    elif transaction == "transfer":
        new_reciever_balance = reciever.balance + Decimal(amount)
        new_sender_balance = sender.balance - Decimal(amount)
        data["reciever_new_balance"] = new_reciever_balance
        data["sender_new_balance"] = new_sender_balance
        reciever.balance = new_reciever_balance
        sender.balance = new_sender_balance
        reciever.save()
        sender.save()
    elif transaction == "withdraw":
        new_sender_balance = sender.balance - Decimal(amount)
        data["sender_new_balance"] = new_sender_balance
        sender.balance = new_sender_balance
        sender.save()
    elif transaction == "deposit":
        new_reciever_balance = reciever.balance + Decimal(amount)
        data["reciever_new_balance"] = new_reciever_balance
        reciever.balance = new_reciever_balance
        reciever.save()
    elif transaction == "loan":
        try:
            loan = Loan.objects.get(account=sender_id)
        except Loan.DoesNotExist:
            loan = None
        if loan:
            loan_balance = loan.left_to_pay
            if Decimal(amount) > loan_balance:
                return Response(
                    {"failure": "Loan balance smaller than what you are trying to pay!"}
                )
            new_loan_balance = loan_balance - Decimal(amount)
            loan.left_to_pay = new_loan_balance
            if loan.left_to_pay == 0:
                loan.delete()
            else:
                loan.save()
            new_sender_balance = sender.balance - Decimal(amount)
            data["sender_new_balance"] = new_sender_balance
            sender.balance = new_sender_balance
            sender.save()
        else:
            return Response({"failure": "You have no Loan"})
    elif transaction == "credit":
        print("entered")
        try:
            card = Card.objects.get(account=sender_id)
            print(card)
        except:
            card = None
        if card:
            card_balance = card.current_credit_used
            if card_balance == 0:
                return Response({"failure": "Credit card not used!"})
            elif Decimal(amount) > card_balance:
                return Response(
                    {"failure": "Your Credit has less the amount you tried to pay!"}
                )
            else:
                new_card_balance = card_balance - Decimal(amount)
                card.current_credit_used = new_card_balance
                card.save()
                new_sender_balance = sender.balance - Decimal(amount)
                data["sender_new_balance"] = new_sender_balance
                sender.balance = new_sender_balance
                sender.save()
        else:
            print("fail")
            return Response({"failure": "You have no Credit Card"})
    print("success")
    new_transaction = TransactionSerializer(data=data)
    if new_transaction.is_valid():
        new_transaction.save()
        return Response(new_transaction.data, status=status.HTTP_201_CREATED)
    return Response(new_transaction.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAuthenticated])
@api_view(["GET"])
def get_transactions(request):
    account = Account.objects.get(user=request.user)
    transactions = Transaction.objects.filter(
        Q(sender_account=account.id) | Q(reciever_account=account.id)
    ).order_by("id")
    serializer = TransactionSerializer(transactions, many=True)
    return Response(serializer.data)
