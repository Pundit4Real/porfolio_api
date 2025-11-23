from rest_framework import serializers
from api.models.testimonials import Testimonial

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = [
            "id",
            "slug",
            "name",
            "role",
            "company",
            "feedback",
            "image",
            "date",
            "rating"
        ]
        read_only_fields = ["id", "slug", "date"]