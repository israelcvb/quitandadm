from django.urls import path

from . import views

app_name = 'website'

urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name='home'),
]
