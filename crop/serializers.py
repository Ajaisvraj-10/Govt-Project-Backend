from rest_framework import serializers
from .models import Category,ProductType,Product,Plant,CropsinFarmer,ProductStock



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        

class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = '__all__'
        

class CropsinFarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CropsinFarmer
        fields = '__all__'
    

class ProductStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductStock
        fields = '__all__'
        

        

        

        

        

