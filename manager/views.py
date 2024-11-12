from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from users.models import BankUser
from users.serializers import BankUserSerializer
from accounts.models import Account
from accounts.serializers import AccountSerializer
from loans.models import Loan
from loans.serializers import LoanSerializer
from cards.models import Card, CreditTransaction
from cards.serializers import CardSerializer, CreditTransactionSerializer
from transactions.models import Transaction
from transactions.serializers import TransactionSerializer


@permission_classes([IsAdminUser])
@api_view(["GET"])
def manager_data(request):
    users = BankUser.objects.all()
    accounts = Account.objects.all()
    loans = Loan.objects.all()
    cards = Card.objects.all()
    credit_transactions = CreditTransaction.object.all()
    transactions = Transaction.objects.all()
    users_serializer = BankUserSerializer(users, many=True)
    accounts_serializer = AccountSerializer(accounts, many=True)
    loans_serializer = LoanSerializer(loans, many=True)
    cards_serializer = CardSerializer(cards, many=True)
    credit_transactions_serializer = CreditTransactionSerializer(
        credit_transactions, many=True
    )
    transactions_serializer = TransactionSerializer(transactions, many=True)
    return Response(
        {
            users: users_serializer.data,
            accounts: accounts_serializer.data,
            loans: loans_serializer.data,
            cards: cards_serializer.data,
            credit_transactions: credit_transactions_serializer.data,
            transactions: transactions_serializer.data,
        }
    )
