from rest_framework import serializers

from app.moduls._access_rights.access_rights_model import AccessRights
from . import reseller_model


class AccessRightsSerializer(serializers.ModelSerializer):

    class Meta:
        model = AccessRights
        fields = ['id', 'name']


class ResellerSerializer(serializers.ModelSerializer):

    access_rights = AccessRightsSerializer()
    class Meta:
        model = reseller_model.Reseller
        fields = ['id', 'name', 'phone', 'email', 'password', 'access_rights']