from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from users.models import BankUser
from users.serializers import BankUserSerializer
from .models import Account
from .serializers import AccountSerializer


@api_view(["POST"])
def auto_create(request):
    user = request.user

    return Response("Account Created Succesfully!")
