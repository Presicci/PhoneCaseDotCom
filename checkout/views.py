# home/views.py
from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def checkout_view(request):
    return render(request, 'checkout.html')
