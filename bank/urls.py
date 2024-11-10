from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("", include("home.urls")),
    path("users/", include("users.urls")),
    path("accounts/", include("accounts.urls")),
    path("transactions/", include("transactions.urls")),
    path("loans/", include("loans.urls")),
    path("cards/", include("cards.urls")),
]
