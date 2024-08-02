from rest_framework import serializers

from . import furniture_model

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = furniture_model.Category
        fields = ['id', 'name']