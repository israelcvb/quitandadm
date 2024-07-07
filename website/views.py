from django.http import HttpResponse
from django.views.generic import CreateView, ListView

from .models import Product

# Create your views here.
def home(request):
    return HttpResponse("Olá, estamos começando a construção do WebApp Quitanda da Dona Maria!")


class CreateProductView(CreateView):
    model = Product
    fields = ['barcode', 'name', 'description', 'price']

class ListProductView(ListView):
    model = Product
    context_object_name = 'products'