from rest_framework import viewsets
from api.models.skills import Skill
from api.serializers.skills import SkillSerializer
from api.utils.hero_mixin import HeroPageMixin


class SkillViewSet(HeroPageMixin,viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    hero_page = "skills"
