from django.urls import path
from . import views

urlpatterns = [
    path("", views.card_request, name="card_request"),
    path("get_form_data/", views.get_form_data, name="get_form_data"),
    path("get_card/", views.get_card, name="get_card"),
    path("use_card/", views.use_card, name="use_card"),
    path("card_history/", views.card_history, name="card_history"),
]
