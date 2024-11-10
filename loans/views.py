from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Loan
from .serializers import LoanSerializer
from accounts.models import Account
from transactions.serializers import TransactionSerializer
import random
from decimal import Decimal


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_loans(request):
    user = request.user
    account = Account.objects.get(user=user)
    try:
        loan = Loan.objects.get(account=account)
        serializer = LoanSerializer(loan)
        return Response(serializer.data)
    except:
        return Response("")


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def request_loan(request):
    def check_loan():
        while True:
            loan_num = str(random.randint(10**8, 2147483647))
            check = Loan.objects.filter(loan_number=loan_num)
            if not check:
                return loan_num

    data = request.data
    account = Account.objects.get(user=request.user)
    check_loan_limit = Loan.objects.filter(account=account.id).count()
    if check_loan_limit >= 1:
        return Response({"failure": "sorry you already have two loans"})
    else:
        data["account"] = account.id
        loan_num = check_loan()
        data["loan_number"] = loan_num
        data["left_to_pay"] = data["amount"]
        loan = LoanSerializer(data=data)
        new_account_balance = account.balance + Decimal(data["amount"])
        if loan.is_valid():
            loan.save()
            loan_transaction = {
                "amount": data["amount"],
                "reciever_account": account.id,
                "transaction_type": "loan",
                "details": "took a loan",
                "reciever_new_balance": new_account_balance,
            }
            transaction_serializer = TransactionSerializer(data=loan_transaction)
            if transaction_serializer.is_valid():
                transaction_serializer.save()
                account.balance = new_account_balance
                account.save()
                return Response(loan.data, status=status.HTTP_201_CREATED)
        return Response(loan.errors, status=status.HTTP_400_BAD_REQUEST)
