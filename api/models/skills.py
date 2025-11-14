from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"
