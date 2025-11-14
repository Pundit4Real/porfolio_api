from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    icon = models.CharField(max_length=100, blank=True)   # name of lucide icon or custom
    price = models.CharField(max_length=100, blank=True)  # optional
    highlight = models.BooleanField(default=False)    
    
    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
        
    def __str__(self):
        return self.title
