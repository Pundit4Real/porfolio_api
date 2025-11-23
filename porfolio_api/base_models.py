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
    slug_source_field: str = "title"  # Default field to generate slug from

    def save(self, *args, **kwargs):
        """
        Auto-generate a unique slug based on a defined source field.
        Falls back to `title`, `name`, or a custom field specified in `slug_source_field`.
        """
        if not self.slug:
            # Determine the field to use for slug
            source_field = getattr(self, "slug_source_field", None)
            value = getattr(self, source_field, None) if source_field else None

            # Fallback to 'title' or 'name' if no valid source field
            if not value:
                value = getattr(self, "title", None) or getattr(self, "name", None)

            if value:
                self.slug = uuslug(value, instance=self, max_length=256)

        super().save(*args, **kwargs)

    class Meta:
        abstract = True