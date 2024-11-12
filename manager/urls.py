from django.urls import path
from . import views

urlpatterns = [path("", views.manager_data, name="manager_data")]
