from django.db import models
from porfolio_api.base_models import SlugBaseModel
from ckeditor.fields import RichTextField
from api.models.projects import Category

class Service(SlugBaseModel):
    title = models.CharField(max_length=150)
    description = RichTextField(blank=True, null=True)
    price = models.CharField(max_length=100, blank=True) 
    icon = models.CharField(max_length=100, blank=True)
    highlight = models.BooleanField(default=False)  
    url = models.URLField(blank=True)
    categories = models.ManyToManyField(Category, related_name='services', blank=True)
    
    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
        
    def __str__(self):
        return self.title
