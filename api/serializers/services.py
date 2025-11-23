from rest_framework import serializers
from api.models.services import Service


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"
        filterset_fields = ['highlight',"is_active"]
