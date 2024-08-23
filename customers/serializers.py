from rest_framework import serializers
from .models import ServiceRequest

class ServiceRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceRequest
        fields = ['id', 'user', 'request_type', 'description', 'status', 'created_at', 'updated_at', 'attachment']
        read_only_fields = ['id', 'user', 'status', 'created_at', 'updated_at']

    def validate_description(self, value):
        if not value or len(value.strip()) == 0:
            raise serializers.ValidationError("Description cannot be empty.")
        return value
