from rest_framework import viewsets
from api.models.experience import Experience
from api.serializers.experience import ExperienceSerializer
from api.utils.hero_mixin import HeroPageMixin


class ExperienceViewSet(HeroPageMixin,viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    hero_page = "experience"
