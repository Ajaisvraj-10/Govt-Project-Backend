from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Countrty,State,District,Panchayats,RevenueVillage,LocalVillage,PostOffice
from .seiralizers import CountrySerializers,StateSerializers,DistrictSerializers,PanchayatsSerializers,RevenueVillageSerializers,LocalVillageSerializers,PostOfficeSerializers

# Create your views here.

class CountrytViewSet(viewsets.ModelViewSet):
    queryset = Countrty.objects.all()
    serializer_class = CountrySerializers
    

class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializers
    
    
class DistrictViewSet(viewsets.ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializers
    

class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializers
    
    
class PanchayatsViewSet(viewsets.ModelViewSet):
    queryset = Panchayats.objects.all()
    serializer_class = PanchayatsSerializers
    

class RevenueVillageViewSet(viewsets.ModelViewSet):
    queryset = RevenueVillage.objects.all()
    serializer_class = RevenueVillageSerializers
    
    
class LocalVillageViewSet(viewsets.ModelViewSet):
    queryset = LocalVillage.objects.all()
    serializer_class = LocalVillageSerializers
    
class PostOfficeViewSet(viewsets.ModelViewSet):
    queryset = PostOffice.objects.all()
    serializer_class = PostOfficeSerializers