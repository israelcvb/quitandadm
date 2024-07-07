from django.urls import path

from . import views

app_name = 'website'

urlpatterns = [
    path('website/', views.home, name='home')
]
