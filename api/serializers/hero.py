from rest_framework import serializers
from api.models.hero import Home, HeroSection


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = "__all__"


class HeroSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroSection
        fields = "__all__"
