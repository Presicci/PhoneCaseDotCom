# home/views.py
from django.shortcuts import render, redirect
from .models import Product
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
from cart.cart import Cart


@csrf_exempt
def home_view(request):
    post_result = request.POST.get("sort", "")
    search_result = request.POST.get("search", None)
    name_filter = request.session.get('name_filter', '')
    if search_result is not None:
        request.session['name_filter'] = search_result
        name_filter = request.session.get('name_filter', '')
    if post_result == 'Price - Low to high':
        query_results = Product.objects.annotate(name_lower=Lower('name')).filter(name_lower__contains=name_filter).order_by('price')
    elif post_result == 'Price - High to low':
        query_results = Product.objects.annotate(name_lower=Lower('name')).filter(name_lower__contains=name_filter).order_by('price') .reverse()
    elif post_result == 'Availability - Low to high':
        query_results = Product.objects.annotate(name_lower=Lower('name')).filter(name_lower__contains=name_filter).order_by('quantity')
    elif post_result == 'Availability - High to low':
        query_results = Product.objects.annotate(name_lower=Lower('name')).filter(name_lower__contains=name_filter).order_by('quantity').reverse()
    elif post_result == 'Alphabetical - Z-A':
        query_results = Product.objects.annotate(name_lower=Lower('name')).filter(name_lower__contains=name_filter).order_by('name').reverse()
    else:
        query_results = Product.objects.annotate(name_lower=Lower('name')).filter(name_lower__contains=name_filter).order_by('name')
    context = {'query_results': query_results}
    return render(request, 'index.html', context)


@login_required(login_url="/users/login")
def cart_add(request, id, place):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    product.quantity += 1
    cart.add(product=product)
    if place == 2:
        return redirect("/checkout/")
    return redirect("/")


@login_required(login_url="/users/login")
def item_clear(request, id, place):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    if place == 2:
        return redirect("/checkout/")
    return redirect("/")


@login_required(login_url="/users/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("/")


@login_required(login_url="/users/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("/")


@login_required(login_url="/users/login")
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')