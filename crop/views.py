from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CategorySerializer,ProductTypeSerializer,ProductSerializer,PlantSerializer,CropsinFarmerSerializer,ProductStockSerializer
from .models import Category,ProductType,Product,Plant,CropsinFarmer,ProductStock


# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    

class ProductTypeViewSet(viewsets.ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
    

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class PlantViewSet(viewsets.ModelViewSet):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
    

class CropsinFarmerViewSet(viewsets.ModelViewSet):
    queryset = CropsinFarmer.objects.all()
    serializer_class = CropsinFarmerSerializer
    

class ProductStockViewSet(viewsets.ModelViewSet):
    queryset = ProductStock.objects.all()
    serializer_class = ProductStockSerializer