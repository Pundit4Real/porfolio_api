from rest_framework import viewsets
from api.models.testimonials import Testimonial
from api.serializers.testimonials import TestimonialSerializer
from api.utils.hero_mixin import HeroPageMixin


class TestimonialViewSet(HeroPageMixin,viewsets.ModelViewSet):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
    hero_page = "testimonials"
