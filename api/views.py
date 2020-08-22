from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product
import django_filters.rest_framework
from rest_framework import status

# Create your views here.

@api_view(['GET'])
def apiOverview(request):

    api_urls = {
        'All Products List' : '/product-list/',
        'Detailed View' : '/product-details/<str:pk>/',
        'Register Product' : '/product-register/',
        'Available Products List' : '/product-list-available/',
        'Out of Stock Products List' : '/product-list-soldout/',
        'Register Product Quantity Change' : '/product-quantity-change/<str:pk>/<str:quantity>/'

    }
    return Response(api_urls)




@api_view(['GET'])
def productList(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def productDetails(request, pk):
    try:
        products = Product.objects.get(sku=pk)
        serializer = ProductSerializer(products, many=False)
        return Response(serializer.data)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def productListAvailable(request):
    products = Product.objects.all().exclude(quantity=0)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def productListSoldOut(request):
    products = Product.objects.filter(quantity=0)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def productRegister(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
def productQuantityChange(request, pk, quantity):
    products = Product.objects.get(sku=pk)
    data = {'quantity': products.quantity + int(quantity)}
    serializer = ProductSerializer(products, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
