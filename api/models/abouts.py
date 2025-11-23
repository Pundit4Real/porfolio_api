from django.db import models
from api.directories import about_directory
from porfolio_api.base_models import SlugBaseModel
from ckeditor.fields import RichTextField

class About(SlugBaseModel):

    bio = RichTextField(blank=True, null=True)    
    image = models.ImageField(upload_to=about_directory, blank=True, null=True)
    expertise = models.ManyToManyField('Expertise', related_name='abouts', blank=True)
    tech_stack = models.ManyToManyField('api.Skill', related_name='abouts', blank=True)
    
    class Meta:
        verbose_name = "About Section"
        verbose_name_plural = "About Sections"

    def __str__(self):
        return "About Section"
    

class Expertise(SlugBaseModel):
    title = models.CharField(max_length=150)
    proficiency_level = models.CharField(max_length=100, blank=True)
    years_of_experience = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Expertise"
        verbose_name_plural = "Expertises"

    def __str__(self):
        return self.title