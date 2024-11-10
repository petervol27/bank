from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_loans, name="get_loans"),
    path("request_loan/", views.request_loan, name="request_loan"),
]
