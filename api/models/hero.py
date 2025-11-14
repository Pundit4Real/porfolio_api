from django.db import models
from api.directories import home_directory

class Home(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    description = models.TextField()
    keywords = models.CharField(max_length=250, blank=True)
    resume = models.FileField(upload_to=home_directory, blank=True, null=True)
    profile_image = models.ImageField(upload_to=home_directory, blank=True, null=True)

    class Meta:
        verbose_name = "Home Section"
        verbose_name_plural = "Home Sections"

    def __str__(self):
        return self.name

class HeroSection(models.Model):
    headline = models.CharField(max_length=200)
    subheadline = models.CharField(max_length=300, blank=True)

    class Meta:
        verbose_name = "Hero Section"
        verbose_name_plural = "Hero Sections"


    def __str__(self):
        return self.headline
