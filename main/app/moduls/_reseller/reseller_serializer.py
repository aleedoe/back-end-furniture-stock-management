from rest_framework import serializers

from . import reseller_model

class ResellerSerializer(serializers.ModelSerializer):

    class Meta:
        model = reseller_model.Reseller
        fields = ['id', 'name', 'phone', 'email', 'password', 'access_rights_id']