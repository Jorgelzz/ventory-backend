from rest_framework import serializers
from .models import Product, InventoryManagement, User


class InventoryManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryManagement
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class UserSerializer(serializers.ModelField):
    class Meta:
        model = User
        fields = "__all__"