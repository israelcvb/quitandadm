from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Olá, estamos começando a construção do WebApp Quitanda da Dona Maria!")