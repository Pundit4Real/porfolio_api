from django.db import models
from porfolio_api.base_models import SlugBaseModel

class Service(SlugBaseModel):
    title = models.CharField(max_length=150)
    description = models.TextField()
    price = models.CharField(max_length=100, blank=True)  # optional
    highlight = models.BooleanField(default=False)    
    
    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
        
    def __str__(self):
        return self.title
