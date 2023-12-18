from django.shortcuts import render,redirect
from rest_framework import generics
from .models import User, Shop, Product, ProductCategory, ProductColor, Cart, Order
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response

def post(request,serializ):
    seri = serializ(data=request.data)

    if seri.is_valid():
        seri.save()
        return Response(seri.data, status=201)
    return Response(seri.errors, status=400)

def put(request,id,serializ,model):
    try:
        obj = model.objects.get(pk=id)
    except model.DoesNotExist:
        return Response(status=404)

    serializer = serializ(obj, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=200)
    return Response(serializer.errors, status=400)

def delete(request,id,model):
    try:
        obj = model.objects.get(pk=id)
    except model.DoesNotExist:
        return Response(status=404)

    obj.delete()
    return Response(status=204)



@api_view(['POST'])
def create_user(request):
    userserializer = UserSerializer(data=request.data)

    if userserializer.is_valid():
        user = userserializer.save()
        tokens = userserializer.get_tokens(user)
        return Response({**userserializer.data, **tokens}, status=201)

    return Response(userserializer.errors, status=400)


@api_view(['POST'])
def create_shop(request):
    if request.method == 'POST':
        shop = post(request,ShopSerializer)
        return shop

@api_view(['PUT'])
def update_shop(request,id):
    if request.method == 'PUT':
        shop = put(request,id,ShopSerializer,Shop)
        return shop

@api_view(['POST','PUT'])
def create_product_category(request):
    if request.method == 'POST':
        cat = post(request,ProductCategorySerializer)
        return cat

    if request.method == 'PUT':
        cat = put(request,ProductCategorySerializer,ProductCategorySerializer)
        return cat

@api_view(['POST','PUT','DELETE'])
def create_product(request):
    if request.method == 'POST':
        prod = post(request,ProductSerializer)
        return prod

@api_view(['PUT'])       
def update_product(request,id):

    if request.method == 'PUT':
        prod = put(request,id,ProductSerializer,Product)
        return prod


@api_view(['POST'])
def create_productcolour(request):
    serializer = ProductColorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def create_cart(request):
    if request.method == 'POST':
        car = post(request,CartSerializer)
        return car
    if request.method == 'PUT':
        car = put(request,CartSerializer,Cart)
        return car
    if request.method == 'DELETE':
        car = delete(request,CartSerializer,Cart)
@api_view(['POST'])
def create_order(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['POST','DELETE'])
def create_review(request):
    review = post(request,ProductReviewSerializer)
    return review

def user_list_dashboard(request):
    users = User.objects.all()
    shop = Shop.objects.all()
    productcategory = ProductCategory.objects.all()
    product = Product.objects.all()
    productcolour = ProductColor.objects.all()
    cart = Cart.objects.all()
    order = Order.objects.all()
    review = ProductReview.objects.all()
    for o in order:
        print(o)
    context = {
        'users': users, "productcategory":productcategory,"product":product,"productcolour":productcolour,"cart":cart,"order":order,"review":review,"shop":shop
    }

    return render(request, 'user_management/users/list.html', context)


def home(request):
    return render(request, 'user_management/users/home.html')

def shop_input(request):
    return render(request, 'user_management/users/shop.html')

def user_input(request):
    return render(request, 'user_management/users/user.html')

def product_input(request):
    return render(request, 'user_management/users/product.html')

def order_input(request):
    return render(request, 'user_management/users/order.html')

def review_input(request):
    return render(request, 'user_management/users/review.html')