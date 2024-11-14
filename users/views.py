from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from users.models import BankUser
from users.serializers import BankUserSerializer
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


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
    user.is_staff = False
    user.save()
    return Response("New user created")


@permission_classes([IsAuthenticated])
@api_view(["GET"])
def get_users(request):
    users = BankUser.objects.exclude(id=request.user.id)
    serializer = BankUserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def validate_token(request):
    check_admin = request.user.is_staff
    return Response({"valid": "token is valid", "check_admin": check_admin})
