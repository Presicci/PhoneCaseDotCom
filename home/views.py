# home/views.py
from django.shortcuts import render
from .models import Product
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def home_view(request):
    post_result = request.POST.get("sort", "")
    search_result = request.POST.get("search", "")
    name_filter = request.session.get('name_filter', '')
    if search_result != '':
        request.session['name_filter'] = search_result
        name_filter = request.session.get('name_filter', '')
    if post_result == 'Price - Low to high':
        query_results = Product.objects.filter(name__contains=name_filter).order_by('price')
    elif post_result == 'Price - High to low':
        query_results = Product.objects.filter(name__contains=name_filter).order_by('price').reverse()
    elif post_result == 'Availability - Low to high':
        query_results = Product.objects.filter(name__contains=name_filter).order_by('quantity')
    elif post_result == 'Availability - High to low':
        query_results = Product.objects.filter(name__contains=name_filter).order_by('quantity').reverse()
    elif post_result == 'Alphabetical - Z-A':
        query_results = Product.objects.filter(name__contains=name_filter).order_by('name').reverse()
    else:
        query_results = Product.objects.filter(name__contains=name_filter).order_by('name')
    context = {'query_results': query_results}
    return render(request, 'todo/templates/index.html', context)
