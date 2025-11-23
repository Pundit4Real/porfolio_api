from django.db import models
from api.models.skills import Skill
from porfolio_api.base_models import SlugBaseModel
from ckeditor.fields import RichTextField
class Experience(SlugBaseModel):
    role = models.CharField(max_length=100)
    company = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=200, blank=True)
    description = RichTextField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    skills_used = models.ManyToManyField(Skill, related_name="experiences")

    class Meta:
        verbose_name = "Experience"
        verbose_name_plural = "Experiences"

    def __str__(self):
        return f"{self.role} at {self.company}"

