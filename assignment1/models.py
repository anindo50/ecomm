from django.db import models

# models.py in your Django app (assignment1 or assignment2)
from django.contrib.auth.models import User

class Shop(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        app_label = 'assignment1'
        
        # Other shop-related fields

class ProductCategory(models.Model):
    name = models.CharField(max_length=100)
    # Other category-related fields

class Product(models.Model):
    name = models.CharField(max_length=100)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    # Other product-related fields

class ProductColor(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.CharField(max_length=50)
    stock = models.PositiveIntegerField(default=0)
    # Other color-related fields

class Cart(models.Model):
    user = models.ForeignKey(Product, on_delete=models.CASCADE)
    products = models.ManyToManyField(ProductColor)
    # Other cart-related fields

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(ProductColor)
    # Other order-related fields

