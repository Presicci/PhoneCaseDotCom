# home/urls.py
from django.urls import path
from .views import checkout_view

app_name = 'checkout'

urlpatterns = [
    path("", checkout_view),
]
