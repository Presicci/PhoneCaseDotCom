# home/views.py
from django.shortcuts import render, redirect

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from cart.cart import Cart
from .models import Product

@csrf_exempt
def checkout_view(request):
    return render(request, 'checkout.html')


@login_required(login_url="/users/login")
def cart_add(request, id, place):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    # return redirect("index.html")
    return redirect("/checkout/")


@login_required(login_url="/users/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("/")


@login_required(login_url="/users/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("/checkout/")


@login_required(login_url="/users/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("/checkout/")


@login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("/")


@login_required(login_url="/users/login")
def cart_detail(request):
    return render(request, '/checkout/')