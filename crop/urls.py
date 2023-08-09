from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . views import CategoryViewSet,ProductTypeViewSet,ProductViewSet,PlantViewSet,CropsinFarmerViewSet,ProductStockViewSet

router = DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'product_type', ProductTypeViewSet)
router.register(r'product', ProductViewSet)
router.register(r'plant', PlantViewSet)
router.register(r'crops_in_farmer', CropsinFarmerViewSet)
router.register(r'product_stock', ProductStockViewSet)

urlpatterns = [
    path('api/crops', include(router.urls)),
    
    
]
