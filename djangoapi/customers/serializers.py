from rest_framework import serializers
from .models import customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = customer
        fields = ['id', 'customer_name', 'customer_email', 'customer_phone', 'customer_address', 'customer_city']