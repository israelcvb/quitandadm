from django.urls import path

from . import views

app_name = 'products'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='list'),
    path('news/', views.ProductCreateView.as_view(), name='create'),
    path('detail/<int:pk>/', views.ProductDetailView.as_view(), name='detail'),
    path('update/<int:pk>', views.ProductUpdateView.as_view(), name='update'),
]
