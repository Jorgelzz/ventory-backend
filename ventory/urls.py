from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, InventoryManagementViewSet, UserViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'inventory-managers', InventoryManagementViewSet)
router.register(r'users', UserViewSet)


urlpatterns = [
    path('', include(router.urls))
]