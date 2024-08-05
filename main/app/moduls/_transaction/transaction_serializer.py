from rest_framework import serializers

from app.moduls._reseller.reseller_model import Reseller
from app.moduls._furniture.furniture_model import Category, Furniture
from . import transaction_model

class ResellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reseller
        fields = ['id', 'name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

class FurnitureSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Furniture
        fields = ['id', 'name', 'category', 'prize']

class TransactionDetailSerializer(serializers.ModelSerializer):
    furniture = FurnitureSerializer()

    class Meta:
        model = transaction_model.TransactionDetail
        fields = ['furniture', 'quantity']

class TransactionSerializer(serializers.ModelSerializer):
    reseller = ResellerSerializer()
    selected_furniture = serializers.SerializerMethodField()
    total_prices = serializers.SerializerMethodField()

    class Meta:
        model = transaction_model.Transaction
        fields = ['id', 'reseller', 'selected_furniture', 'status', 'created_at', 'total_prices']

    def get_selected_furniture(self, obj):
        details = transaction_model.TransactionDetail.objects.filter(transaction=obj)
        return TransactionDetailSerializer(details, many=True).data

    def get_total_prices(self, obj):
        details = transaction_model.TransactionDetail.objects.filter(transaction=obj)
        total = sum(detail.furniture.prize * detail.quantity for detail in details)
        return total