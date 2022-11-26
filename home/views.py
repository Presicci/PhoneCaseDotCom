# home/views.py
from django.shortcuts import render
from .models import Product


def home_view(request):
    query_results = Product.objects.all()
    post_result = request.POST.get("sort", "")
    if post_result == 'Price - Low to high':
        query_results = Product.objects.all().order_by('price')
    elif post_result == 'Price - High to low':
        query_results = Product.objects.all().order_by('price').reverse()
    elif post_result == 'Availability - Low to high':
        query_results = Product.objects.all().order_by('quantity')
    elif post_result == 'Availability - High to low':
        query_results = Product.objects.all().order_by('quantity').reverse()
    elif post_result == 'Alphabetical - Z-A':
        query_results = Product.objects.all().order_by('name').reverse()
    else:
        query_results = Product.objects.all().order_by('name')
    context = {'query_results': query_results}
    return render(request, 'todo/index.html', context)
