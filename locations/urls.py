from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CountrytViewSet,StateViewSet,DistrictViewSet,PanchayatsViewSet,RevenueVillageViewSet,LocalVillageViewSet


router = DefaultRouter()
router.register(r'country', CountrytViewSet)
router.register(r'state', StateViewSet)
router.register(r'district', DistrictViewSet)
router.register(r'panchayats', PanchayatsViewSet)
router.register(r'revenue_village', RevenueVillageViewSet)
router.register(r'local_village', LocalVillageViewSet)

urlpatterns = [
    path('api/locations', include(router.urls)),
]