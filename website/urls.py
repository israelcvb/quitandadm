from django.urls import path

from . import views

app_name = 'website'

urlpatterns = [
    path('website/', views.home, name='home'),
    path('produtos/novo', views.CreateProductView.as_view(), name='new_product'),
    path('produtos/', views.ListProductView.as_view(), name='products'),
]
