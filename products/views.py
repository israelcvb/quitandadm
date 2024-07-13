from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from . models import Product


# Create your views here.
class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('products:list')

class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'


class ProductListView(ListView):
    model = Product
    context_object_name = 'products'


class ProductUpdateView(UpdateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('products:list')