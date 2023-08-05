from rest_framework import serializers
from .models import FPO, AEO, ICS, VFC, Farmers



class FPOSerializer(serializers.ModelSerializer):
    class Meta:
        model = FPO
        fields = '__all__'
        

class AEOSerializer(serializers.ModelSerializer):
    class Meta:
        model = AEO
        fields = '__all__'
        
        

class ICSSerializer(serializers.ModelSerializer):
    class Meta:
        model = ICS
        fields = '__all__'
        
        
        
        
class VFCLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VFC
        fields = ['local_village']
        
        

class VFCSerializer(serializers.ModelSerializer):
    class Meta:
        model = VFC
        fields = '__all__'

        

class FarmersLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmers
        fields = ['panchayats']


class FarmersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmers
        fields = '__all__'
        
        
