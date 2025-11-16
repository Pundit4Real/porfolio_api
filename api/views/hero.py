from rest_framework import viewsets
from api.models.hero import Home, HeroSection
from api.serializers.hero import HomeSerializer, HeroSectionSerializer


class HomeViewSet(viewsets.ModelViewSet):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer


class HeroSectionViewSet(viewsets.ModelViewSet):
    queryset = HeroSection.objects.all()
    serializer_class = HeroSectionSerializer
