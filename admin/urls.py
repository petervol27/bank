from django.urls import path
from . import views

urlpatterns = [path("", views.get_admin_data, name="get_admin_data")]
