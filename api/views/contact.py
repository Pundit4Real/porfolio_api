from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from api.models.contact import ContactMessage, ContactInfo
from api.serializers.contact import ContactMessageSerializer, ContactInfoSerializer
from api.utils.contact_email import send_contact_message, send_contact_success_message
from api.utils.hero_mixin import HeroPageMixin

class ContactMessageViewSet(HeroPageMixin, viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all().order_by('-created_at')
    serializer_class = ContactMessageSerializer
    hero_page = "contact"

    def perform_create(self, serializer):
        message = serializer.save() 

        # Notify admin
        send_contact_message(
            name=message.name,
            email=message.email,
            subject=getattr(message, "subject", "New Message"),
            message=message.message,
            phone=getattr(message, "phone", None)
        )

        # Acknowledgement email to sender
        send_contact_success_message(message.name, message.email)

    @action(detail=True, methods=["post"])
    def mark_responded(self, request, pk=None):
        message = self.get_object()

        message.responded = True
        message.responded_at = timezone.now()
        message.response_message = request.data.get("response_message", "")

        message.save()

        return Response({"status": "marked as responded"})


class ContactInfoViewSet(HeroPageMixin,viewsets.ModelViewSet):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer
    hero_page = "contact"
