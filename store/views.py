from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .serializers import RegisterSerializer, LoginSerializer, NewsletterSerializer
from .models import NewsletterSubscriber

# Create your views here.
@api_view(['GET'])
def api_home(request):
    return Response({
        'message': 'Next Store backend is running successfully'
    })


@api_view(['GET'])
def api_home(request):
    return Response({
        "message": "Next Store API running"
    })


@api_view(['GET'])
def product_list(request):
    category = request.GET.get("category")

    if category:
        products = Product.objects.filter(category__name=category)
    else:
        products = Product.objects.all()

    serializer = ProductSerializer(products, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def product_detail(request, pk):
    product = Product.objects.get(id=pk)

    serializer = ProductSerializer(product)

    return Response(serializer.data)


@api_view(['GET'])
def category_list(request):
    categories = Category.objects.all()

    serializer = CategorySerializer(categories, many=True)

    return Response(serializer.data)

# create order api
from .models import Order, OrderItem


@api_view(['POST'])
def create_order(request):

    data = request.data

    order = Order.objects.create(
        first_name=data["first_name"],
        last_name=data["last_name"],
        email=data["email"],
        address=data["address"],
        city=data["city"],
        pin_code=data["pin_code"],
        total_amount=0
    )

    total = 0

    for item in data["items"]:

        product = Product.objects.get(id=item["product_id"])

        quantity = item["quantity"]

        price = product.price

        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=quantity,
            price=price
        )

        total += price * quantity

    order.total_amount = total
    order.save()

    return Response({
        "message": "Order placed successfully",
        "order_id": order.id
    })
    
# account api
@api_view(['POST'])
def register_user(request):

    serializer = RegisterSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response({
            "message": "User registered successfully"
        })

    return Response(serializer.errors)


@api_view(['POST'])
def login_user(request):

    serializer = LoginSerializer(data=request.data)

    if serializer.is_valid():

        username = serializer.validated_data["username"]
        password = serializer.validated_data["password"]

        user = authenticate(username=username, password=password)

        if user:

            return Response({
                "message": "Login successful",
                "username": user.username
            })

        else:

            return Response({
                "error": "Invalid credentials"
            })

    return Response(serializer.errors)


@api_view(['POST'])
def subscribe_newsletter(request):

    serializer = NewsletterSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response({
            "message": "Subscribed successfully"
        })

    return Response(serializer.errors)