from django.db import models
from api.models.skills import Skill
from api.directories import project_image_directory
from porfolio_api.base_models import SlugBaseModel

class Project(SlugBaseModel):
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=250, blank=True)
    description = models.TextField()
    live_link = models.URLField(blank=True)
    live_demo = models.URLField(blank=True)
    github_link = models.URLField(blank=True)
    tags = models.CharField(max_length=200, blank=True)
    category = models.ManyToManyField('Category', related_name='projects', blank=True)
    tech_stack = models.ManyToManyField(Skill, related_name='projects', blank=True)

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=project_image_directory)

    class Meta:
        verbose_name = "Project Image"
        verbose_name_plural = "Project Images"

    def __str__(self):
        return f"Image for {self.project.title}"