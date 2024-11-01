from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from users.models import BankUser
from users.serializers import BankUserSerializer
from .models import Account
from .serializers import AccountSerializer
import random


@api_view(["POST"])
def auto_create(request):
    def check_account():
        while True:
            account_num = str(random.randint(10**8, 10**12 - 1))
            check = Account.objects.filter(account_num=account_num)
            if not check:
                return account_num

    account_num = check_account()
    user = request.user
    account = Account.objects.create(
        balance=0,
        branch=random.randint(100, 999),
        status=True,
        user=user,
        account_num=account_num,
    )
    account.save()
    return Response("Account Created Succesfully!")


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_account(request):
    if request.user.is_staff:
        print("admin!")
    account = Account.objects.get(user=request.user)
    username = request.user.username.capitalize()
    serializer = AccountSerializer(account)
    return Response({"account": serializer.data, "username": username})
