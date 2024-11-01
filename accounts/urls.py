from django.urls import path
from . import views

urlpatterns = [path("auto_create/", views.auto_create, name="auto_create_account")]
