from rest_framework import viewsets
from api.models.services import Service
from api.serializers.services import ServiceSerializer
from api.utils.hero_mixin import HeroPageMixin


class ServiceViewSet(HeroPageMixin,viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    filterset_fields = ['highlight',"is_active"]
    hero_page = "services"
