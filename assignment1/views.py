from django.shortcuts import render
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

def put(request,serializ,model):
    name = request.data.get('name')  
    if not name:
        return Response(status=400)

    try:
        obj = model.objects.get(name=name)
        serializer = serializ(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    except model.DoesNotExist:
        return Response(status=404)

def delete(request,serializ,model):
    name = request.data.get('name') 
    if not name:
        return Response(status=400)

    try:
        product = model.objects.get(name=name)
        product.delete()
        return Response(status=204)
    except model.DoesNotExist:
        return Response(status=404)



@api_view(['POST'])
def create_user(request):
    userserializer = UserSerializer(data=request.data)

    if userserializer.is_valid():
        user = userserializer.save()
        tokens = userserializer.get_tokens(user)
        return Response({**userserializer.data, **tokens}, status=201)

    return Response(userserializer.errors, status=400)


@api_view(['POST','PUT'])
def create_shop(request):
    if request.method == 'POST':
        serializer = ShopSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    if request.method == 'PUT':
        shop = put(request,ShopSerializer,Shop)
        return shop

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

@api_view(['POST','DELETE'])
def create_review(request):
    review = post(request,ProductReviewSerializer)
    return review

def user_list_dashboard(request):
    users = User.objects.all()
    productcategory = ProductCategory.objects.all()
    product = Product.objects.all()
    productcolour = ProductColor.objects.all()
    cart = Cart.objects.all()
    order = Order.objects.all()
    review = ProductReview.objects.all()
    for o in order:
        print(o)
    context = {
        'users': users, "productcategory":productcategory,"product":product,"productcolour":productcolour,"cart":cart,"order":order,"review":review
    }

    return render(request, 'user_management/users/list.html', context)


def home(request):
    return render(request, 'user_management/users/home.html')

