from rest_framework import serializers

from . import administrator_model

class AdministratorSerializer(serializers.ModelSerializer):

    class Meta:
        model = administrator_model.Administrator
        fields = '__all__'