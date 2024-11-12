from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("register/", views.register, name="register"),
    path("all/", views.get_users, name="get_users"),
    path("validate/", views.validate_token, name="validate"),
]
