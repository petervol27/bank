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
def get_admin_data(request):
    users = BankUser.objects.all()

    return Response("nigga")
