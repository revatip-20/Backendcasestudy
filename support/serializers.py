from rest_framework import serializers
from .models import SupportRepresentative
from customers.serializers import ServiceRequestSerializer

class SupportRepresentativeSerializer(serializers.ModelSerializer):
    assigned_requests = ServiceRequestSerializer(many=True, read_only=True)

    class Meta:
        model = SupportRepresentative
        fields = ['id', 'user', 'assigned_requests']
        read_only_fields = ['id', 'user']
