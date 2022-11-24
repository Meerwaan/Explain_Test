from django.db import models

# Create your models here.
class Territories(models.Model):
    code = models.IntegerField()
    name = models.CharField(max_length=255)
    kind = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    is_current = models.BooleanField(default=False)
    population = models.IntegerField()
    official_website_url = models.CharField(max_length=255)
    articles_count = models.IntegerField()
    admin_docs_count = models.IntegerField()
    impacters_count = models.IntegerField()
    websites_count = models.IntegerField()
    sources_count = models.IntegerField()

class TerritoriesParents(models.Model):
    child_id = models.IntegerField()
    parent_id = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

