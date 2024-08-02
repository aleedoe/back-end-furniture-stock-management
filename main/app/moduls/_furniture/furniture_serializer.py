from rest_framework import serializers

from . import furniture_model

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = furniture_model.Category
        fields = ['id', 'name']

class FurnitureSerializer(serializers.ModelSerializer):

    class Meta:
        model = furniture_model.Furniture
        fields = ['id', 'name', 'prize', 'quantity', 'description', 'attributes', 'category_id', 'warehouser_id']