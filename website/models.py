from django.db import models

# Create your models here.
class Product(models.Model):
    barcode = models.CharField(max_length=32, null=False, blank=False, unique=True)
    name = models.CharField(max_length=64, null=False, blank=False, unique=True)
    description = models.TextField(max_length=512)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)
    created_in = models.DateTimeField(auto_now_add=True)
    modified_in = models.DateTimeField(auto_now=True)

objects = models.Manager()