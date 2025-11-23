from rest_framework import viewsets
from rest_framework.response import Response
from api.models.testimonials import Testimonial
from api.serializers.testimonials import TestimonialSerializer
from api.utils.hero_mixin import HeroPageMixin

class TestimonialViewSet(HeroPageMixin, viewsets.ModelViewSet):
    queryset = Testimonial.objects.all().order_by("-date")
    serializer_class = TestimonialSerializer
    hero_page = "testimonials"

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        # Global stats appear only once
        stats = Testimonial.get_stats()

        return Response({
            "hero": self.get_hero_data(),
            "stats": stats,
            "data": serializer.data
        })
