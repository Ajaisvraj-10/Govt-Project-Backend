from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserDetailsViewSet

router = DefaultRouter()
router.register(r'users', UserDetailsViewSet)


urlpatterns = [
    path('api/users', include(router.urls)),
    
    
]