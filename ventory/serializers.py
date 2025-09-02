from rest_framework import serializers
from django.db.models import F
from django.db import transaction
from .models import Product, InventoryManagement, Stock_balance, User, MovementType


class InventoryManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryManagement
        fields = "__all__"

    def validate(self, attrs):
        if attrs["status"] == MovementType.EXIT or attrs["status"] == MovementType.TRANSFER:
            prod = attrs["product"]
            if attrs["quantity"] > prod.quantity:
                raise serializers.ValidationError("Estoque insuficiente")
        return attrs
        
    @transaction.atomic
    def create(self, validated):

        prod = validated["product"]
        qtd = validated["quantity"]

        InventoryManagement.objects.create(
            product=prod,
            quantity=qtd,
            status=MovementType.EXIT,
            username=validated["username"],
            localization=validated["localization"]
        )
        InventoryManagement.objects.create(
            product=prod,
            quantity=qtd,
            status=MovementType.ENTRY,
            username=validated["username"],
            localization=validated["localization"]
        )

        if validated["status"] == MovementType.ENTRY:
            Product.objects.filter(pk=prod.pk).update(quantity=F("quantity") + qtd)
        else:
            Product.objects.filter(pk=prod.pk).update(quantity=F("quantity") - qtd)

        return super().create(validated)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

        def create(self, validated):
            product = super().create(validated)
            Stock_balance.objects.create(
                product=product,
                localization=validated["localization"],
                quantity=validated["initial_quantity"]
            )
            Product.objects.filter(pk=product.pk).update(quantity=F("quantity") + validated["initial_quantity"])
            return product

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"