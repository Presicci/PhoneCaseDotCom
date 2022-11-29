# home/urls.py
from django.urls import path
from .views import checkout_view
from . import views

app_name = 'checkout'

urlpatterns = [
    path("", checkout_view),
    path('cart/add/<int:id>/<int:place>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/<int:place>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/', views.cart_detail, name='cart_detail')
]