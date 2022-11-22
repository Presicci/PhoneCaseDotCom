# home/views.py
from django.views.generic import ListView
from .models import Product


class HomePageView(ListView):
    model = Product
    template_name = "todo/index.html"

    def get_context_data(self, **kwargs):
        query_results = Product.objects.all()
        context = { 'query_results' : query_results }
        return context
