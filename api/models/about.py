from django.db import models
from api.directories import about_directory

class About(models.Model):
    bio = models.TextField()
    image = models.ImageField(upload_to=about_directory, blank=True, null=True)
    expertise = models.ManyToManyField('Expertise', related_name='abouts', blank=True)
    tech_stack = models.ManyToManyField('api.models.skills.Skill', related_name='abouts', blank=True)
    
    class Meta:
        verbose_name = "About Section"
        verbose_name_plural = "About Sections"

    def __str__(self):
        return "About Section"
    


class Expertise(models.Model):
    title = models.CharField(max_length=150)

    class Meta:
        verbose_name = "Expertise"
        verbose_name_plural = "Expertises"

    def __str__(self):
        return self.title