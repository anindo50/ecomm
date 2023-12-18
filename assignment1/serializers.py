from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken

class UserSerializer(serializers.ModelSerializer):
    tokens = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["username", "password", "tokens"]

    def get_tokens(self, user):
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


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

    def validate(self, data):
        products = data.get('products', [])
        if not products:
            raise serializers.ValidationError("An order must contain at least one product.")
        return data

class ProductReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReview
        fields = ['user', 'product', 'content']  