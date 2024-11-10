from django.urls import path
from . import views

urlpatterns = [
    path("types/", views.transaction_types, name="transaction_types"),
    path("", views.makeTransaction, name="make transaction"),
    path("history/", views.get_transactions, name="history"),
]
