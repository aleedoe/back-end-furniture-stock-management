from rest_framework import serializers

from . import warehouser_model

class WarehouserSerializer(serializers.ModelSerializer):

    class Meta:
        model = warehouser_model.Warehouser
        fields = ['id', 'name', 'phone', 'email', 'password', 'access_rights_id']