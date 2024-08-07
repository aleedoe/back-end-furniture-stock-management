from rest_framework import serializers

from . import furniture_model

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = furniture_model.Category
        fields = ['id', 'name']

class FurnitureSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = furniture_model.Furniture
        fields = ['id', 'name', 'prize', 'quantity', 'description', 'attributes', 'category']