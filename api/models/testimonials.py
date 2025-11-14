from django.db import models

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, blank=True)
    company = models.CharField(max_length=150, blank=True)
    feedback = models.TextField()
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    happy_client = models.IntegerField(default=1)
    average_rating = models.FloatField(default=5.0)
    satisfaction_rate = models.FloatField(default=100.0)

    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"

    def __str__(self):
        return f"{self.name} - {self.company}"


