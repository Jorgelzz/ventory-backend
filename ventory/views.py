from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from .models import InventoryManagement, Product, User
from .serializers import InventoryManagementSerializer, UserSerializer, ProductSerializer
# Create your views here.

class InventoryManagementViewSet(viewsets.ModelViewSet):
    queryset = InventoryManagement.objects.all()
    serializer_class = InventoryManagementSerializer
    filter_backends = [OrderingFilter]
    ordering = ['product']

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [OrderingFilter]
    ordering = ['product_name', 'localization']

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [OrderingFilter]
    ordering = ['username']