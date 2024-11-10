from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
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
        branch=random.choice([choice[0] for choice in Account.BRANCH_CHOICES]),
        status=True,
        user=user,
        account_num=account_num,
    )
    account.save()
    return Response("Account Created Succesfully!")


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_account(request):
    account = Account.objects.get(user=request.user)
    lname = request.user.last_name
    fname = request.user.first_name
    serializer = AccountSerializer(account)
    return Response(
        {"account": serializer.data, "user": {"lname": lname, "fname": fname}}
    )


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_all_accounts(request):
    accounts = Account.objects.all()
    serializer = AccountSerializer(accounts, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_branch_choices(request):
    choices = [
        {"number": choice[0], "name": choice[1]} for choice in Account.BRANCH_CHOICES
    ]
    return Response(choices)
