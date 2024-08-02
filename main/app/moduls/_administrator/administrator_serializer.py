from rest_framework import serializers

from . import administrator_model

class AdministratorSerializer(serializers.ModelSerializer):

    class Meta:
        model = administrator_model.Administrator
        # fields = ['id', 'customer_name', 'phone', 'email', 'password', 'total_orders']