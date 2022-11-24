from django.db import models

# Create your models here.
class Territories(models.Model):
    code=models.CharField(max_length=255)
    name=models.CharField(max_length=255)
    kind=models.CharField(max_length=255)
    created_at=models.DateTimeField()
    updated_at=models.DateTimeField()
    is_current = models.BooleanField(default=False)
    population = models.CharField(max_length=255)
    official_website_url = models.CharField(max_length=255)
    articles_count = models.CharField(max_length=255)
    admin_docs_count = models.CharField(max_length=255)
    impacters_count = models.CharField(max_length=255)
    websites_count = models.CharField(max_length=255)
    sources_count = models.CharField(max_length=255)


class TerritoriesParents(models.Model):
    child_id = models.CharField(max_length=255)
    parent_id = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

