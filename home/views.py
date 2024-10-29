from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.


@api_view(["GET"])
def welcome_page(request):
    info = {
        "message": "Welcome to My Django API",
        "endpoints": {
            "home": "/",
            "api_root": "/api/",
            "users": "/api/users/",
            "products": "/api/products/",
        },
        "note": "Use these endpoints to interact with the API.",
    }
    return Response(info)
