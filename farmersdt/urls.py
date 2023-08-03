from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FPOViewSet, AEOViewSet, ICSViewSet, VFCViewSet, FarmersViewSet

router = DefaultRouter()
router.register(r'fpos', FPOViewSet)
router.register(r'aeos', AEOViewSet)
router.register(r'ics', ICSViewSet)
router.register(r'vfcs', VFCViewSet)
router.register(r'farmers', FarmersViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
