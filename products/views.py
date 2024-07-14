from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from . forms import SearchForm
from . models import Product


class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'
    extra_context = {'context': 'create'}
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
    extra_context = {'context': 'update'}
    success_url = reverse_lazy('products:list')


def custom_404(request):
    return render(request, 'website/404.html', {}, status=404)

def search_form(request):
    if request.method == 'POST':
        sform = SearchForm(request.POST)
        if sform.is_valid():
            barcode = request.POST.get('barcode')
            product = Product.objects.filter(barcode=str(barcode)).first()
            if not product:
                return custom_404(request)
            return redirect('products:detail', pk=product.id)
    else:
        sform = SearchForm()
    return render(request, 'products/search_form.html', {'sform': sform})