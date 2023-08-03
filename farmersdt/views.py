from django.shortcuts import render
from rest_framework import viewsets
from .models import FPO, AEO, ICS, VFC, Farmers
from .serializers import (
    FPOSerializer,
    AEOSerializer,
    ICSSerializer,
    VFCSerializer,
    FarmersSerializer,
)


# Create your views here.

class FPOViewSet(viewsets.ModelViewSet):
    queryset = FPO.objects.all()
    serializer_class = FPOSerializer
    
    

class AEOViewSet(viewsets.ModelViewSet):
    queryset = AEO.objects.all()
    serializer_class = AEOSerializer



class ICSViewSet(viewsets.ModelViewSet):
    queryset = ICS.objects.all()
    serializer_class = ICSSerializer



class VFCViewSet(viewsets.ModelViewSet):
    queryset = VFC.objects.all()
    serializer_class = VFCSerializer



class FarmersViewSet(viewsets.ModelViewSet):
    queryset = Farmers.objects.all()
    serializer_class = FarmersSerializer
