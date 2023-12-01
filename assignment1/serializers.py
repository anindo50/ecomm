from rest_framework import serializers
from .models import User,Shop,ProductCategory,Product,ProductColor,Cart,Order

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]  


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ["name", "owner"]


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ["name"]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name","shop","category"]


class ProductColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductColor
        fields = ["product","color","stock"]

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ["user","products"]

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["user","products"]
