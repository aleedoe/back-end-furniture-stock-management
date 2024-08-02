from rest_framework import serializers

from . import administrator_model

class AdministratorSerializer(serializers.ModelSerializer):

    class Meta:
        model = administrator_model.Administrator
        fields = ['id', 'name', 'phone', 'email', 'password', 'access_rights_id']