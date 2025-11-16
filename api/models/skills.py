from django.db import models
from porfolio_api.base_models import SlugBaseModel

class Skill(SlugBaseModel):
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"

    def __str__(self):
        return self.name
