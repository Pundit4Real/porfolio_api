from rest_framework import serializers
from api.models.services import Service
from api.serializers.projects import CategorySerializer


class ServiceSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()

    class Meta:
        model = Service
        fields = "__all__"
        filterset_fields = ['highlight', "is_active", 'category']

    def get_category(self, obj):
        if obj.category:
            return [CategorySerializer(obj.category).data]
        return []
