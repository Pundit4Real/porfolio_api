from rest_framework import serializers
from api.models.services import Service
from api.serializers.projects import CategorySerializer


class ServiceSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Service
        fields = "__all__"
        filterset_fields = ['highlight', "is_active", 'categories']
