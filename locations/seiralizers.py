from rest_framework import serializers
from .models import Countrty,State,District,Panchayats,RevenueVillage,LocalVillage,PostOffice


class CountrySerializers(serializers.ModelSerializer):
    class Meta:
        model = Countrty
        fields = '__all__'
        
        
class StateSerializers(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'
 
 
class DistrictSerializers(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = '__all__'
        
        
class PanchayatsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Panchayats
        fields = '__all__'
        
        
class RevenueVillageSerializers(serializers.ModelSerializer):
    class Meta:
        model = RevenueVillage
        fields = '__all__'
        
        
class LocalVillageSerializers(serializers.ModelSerializer):
    class Meta:
        model = LocalVillage
        fields = '__all__'


class PostOfficeSerializers(serializers.ModelSerializer):
    class Meta:
        model = PostOffice
        fields = '__all__'

        
            

        