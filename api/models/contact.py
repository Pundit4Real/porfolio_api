from django.db import models
from porfolio_api.base_models import SlugBaseModel
from api.models.services import Service

class ContactMessage(SlugBaseModel):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    service = models.ForeignKey( Service, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="contact_messages"
    )
    message = models.TextField()
    responded = models.BooleanField(default=False)
    responded_at = models.DateTimeField(null=True, blank=True)
    response_message = models.TextField(blank=True)

    class Meta:
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"
        ordering = ['-created_at']

    def __str__(self):
        return f"Message from {self.name} <{self.email}>"       


class ContactInfo(models.Model):
    headline = models.CharField(max_length=200, blank=True)
    subheadline = models.CharField(max_length=400, blank=True)
    address = models.CharField(max_length=300, blank=True)
    phone = models.CharField(max_length=70, blank=True)
    email = models.EmailField(blank=True)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    telegram = models.URLField(blank=True)

    class Meta:
        verbose_name = "Contact Information"
        verbose_name_plural = "Contact Informations"

    def __str__(self):
        return "Contact Information"    
