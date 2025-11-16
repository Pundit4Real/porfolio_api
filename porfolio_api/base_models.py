import uuid
from django.db import models
from uuslug import uuslug


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    views = models.BigIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def increase_views(self):
        self.views += 1
        self.save()

    class Meta:
        abstract = True


class SlugBaseModel(BaseModel):
    slug = models.SlugField(max_length=256, unique=True, editable=False)

    def save(self, *args, **kwargs):
        # Check for 'title' or 'name' to generate the slug
        title_or_name = getattr(self, "title", None) or getattr(self, "name", None)

        if title_or_name:
            # Generate the slug only if 'title' or 'name' is available
            self.slug = uuslug(title_or_name, instance=self)

        super().save(*args, **kwargs)

    class Meta:
        abstract = True