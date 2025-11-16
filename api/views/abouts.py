from rest_framework import viewsets
from api.models.abouts import About, Expertise
from api.serializers.abouts import AboutSerializer, ExpertiseSerializer
from api.utils.hero_mixin import HeroPageMixin

class ExpertiseViewSet(HeroPageMixin,viewsets.ModelViewSet):
    queryset = Expertise.objects.all()
    serializer_class = ExpertiseSerializer
    hero_page = "skills" 

class AboutViewSet(HeroPageMixin,viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    hero_page = "about"
