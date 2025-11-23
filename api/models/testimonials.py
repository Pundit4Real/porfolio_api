from django.db import models
from django.db.models import Avg
from api.directories import testimonial_directory
from porfolio_api.base_models import SlugBaseModel

class Testimonial(SlugBaseModel):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, blank=True)
    company = models.CharField(max_length=150, blank=True)
    feedback = models.TextField()
    image = models.ImageField(upload_to=testimonial_directory, blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    rating = models.FloatField(default=5.0)

    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"

    def __str__(self):
        return f"{self.name} - {self.company}"

    @property
    def length(self):
        """Total number of testimonials in the system."""
        return Testimonial.objects.count()

    @staticmethod
    def get_stats():
        """Returns site-level metrics."""
        qs = Testimonial.objects.all()
        average_rating = qs.aggregate(avg=Avg("rating"))["avg"] or 0
        happy_clients = qs.filter(rating__gte=3).count()
        satisfaction_rate = (average_rating / 5) * 100 if average_rating else 0

        return {
            "happy_clients": happy_clients,
            "average_rating": round(average_rating, 2),
            "satisfaction_rate": round(satisfaction_rate, 2),
            "total_testimonials": qs.count()
        }
