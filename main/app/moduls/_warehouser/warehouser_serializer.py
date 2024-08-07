from rest_framework import serializers

from app.moduls._access_rights.access_rights_model import AccessRights
from . import warehouser_model

class AccessRightsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessRights
        fields = ['id', 'name']

class WarehouserSerializer(serializers.ModelSerializer):

    access_rights = AccessRightsSerializer()
    class Meta:
        model = warehouser_model.Warehouser
        fields = ['id', 'name', 'phone', 'email', 'password', 'access_rights']