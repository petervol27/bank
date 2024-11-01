from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from users.models import BankUser
from users.serializers import BankUserSerializer
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError


# Create your views here.
@api_view(["POST"])
def register(request):
    email = request.data["email"]
    try:
        EmailValidator()(email)
    except ValidationError:
        return Response("Email should be valid!!!")
    user = BankUser.objects.create_user(
        username=request.data["username"],
        email=email,
        password=request.data["password"],
        phone=request.data["phone"],
        first_name=request.data["fname"],
        last_name=request.data["lname"],
        address=request.data["address"],
        citizen_num=request.data["citizen_num"],
    )
    user.is_active = True
    user.save()
    return Response("New user created")
