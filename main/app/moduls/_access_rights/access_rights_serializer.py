from rest_framework import serializers

from . import access_rights_model

class AccessRightsSerializer(serializers.ModelSerializer):
    class Meta:
        model = access_rights_model.AccessRights
        fields = ['id', 'name']