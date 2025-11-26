from rest_framework import serializers
from api.models.contact import ContactMessage, ContactInfo
from api.models.services import Service

class ContactMessageSerializer(serializers.ModelSerializer):
    service = serializers.PrimaryKeyRelatedField(
        queryset=Service.objects.all(),
        required=False,
        allow_null=True
    )

    service_details = serializers.SerializerMethodField()

    class Meta:
        model = ContactMessage
        fields = "__all__"

    def get_service_details(self, obj):
        if obj.service:
            return {
                "id": obj.service.id,
                "title": obj.service.title,
                "price": obj.service.price,
                "icon": obj.service.icon,
            }
        return None



class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = "__all__"
