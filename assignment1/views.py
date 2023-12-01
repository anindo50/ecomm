from django.shortcuts import render
from rest_framework import generics
from .models import User, Shop, Product, ProductCategory, ProductColor, Cart, Order
from .serializers import UserSerializer,ShopSerializer,ProductCategorySerializer,ProductSerializer,ProductColorSerializer,CartSerializer,OrderSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response



@api_view(['POST'])
def create_user(request):
    userserializer = UserSerializer(data=request.data)

    if userserializer.is_valid():
        userserializer.save()
        print("user ok")
    
        return Response(userserializer.data, status=201)
    return Response(userserializer.errors, status=400)

@api_view(['POST'])
def create_shop(request):
    serializer = ShopSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def create_product_category(request):
    serializer = ProductCategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def create_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def create_productcolour(request):
    serializer = ProductColorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def create_cart(request):
    serializer = CartSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
    

@api_view(['POST'])
def create_order(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

def user_list_dashboard(request):
    users = User.objects.all()
    productcategory = ProductCategory.objects.all()
    product = Product.objects.all()
    productcolour = ProductColor.objects.all()
    cart = Cart.objects.all()
    order = Order.objects.all()
    context = {
        'users': users, "productcategory":productcategory,"product":product,"productcolour":productcolour,"cart":cart,"order":order
    }

    return render(request, 'user_management/users/list.html', context)


def home(request):
    return render(request, 'user_management/users/home.html')

