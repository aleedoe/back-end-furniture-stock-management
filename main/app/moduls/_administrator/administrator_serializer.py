from rest_framework import serializers

from app.moduls._access_rights.access_rights_model import AccessRights
from . import administrator_model


class AccessRightsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessRights
        fields = ['id', 'name']

class AdministratorSerializer(serializers.ModelSerializer):
    
    access_rights = AccessRightsSerializer()
    class Meta:
        model = administrator_model.Administrator
        fields = ['id', 'name', 'phone', 'email', 'password', 'access_rights']