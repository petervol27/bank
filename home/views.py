from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.


@api_view(["GET"])
def welcome_page(request):
    info = {
        "message": "Welcome to My Bank API",
        "endpoints": {
            "home": "/",
            "accounts": "/accounts/",
            "users": "/users/",
            "transactions": "/transactions/",
            "loans": "/loans/",
            "cards": "/cards/",
            "token": {"login": "users/login/", "refresh": "/refresh/"},
        },
        "note": "Use these endpoints to interact with the API, though they only work with authentication...so you know...security!",
    }
    return Response(info)
