from django.db import models

# Create your models here.

class Territories(models.Model):
    code = models.CharField (max_lenght = 255)
    name = models.CharField (max_lenght = 255)
    kind = models.CharField (max_lenght = 255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    is_current = models.BooleanField(default=False)
    population = models.CharField(max_lenght= 255)
    official_website_url = models.CharField(max_lenght= 255)
    articles_count = models.CharField(max_lenght= 255)
    admin_docs_count = models.CharField(max_lenght= 255)
    impacters_count = models.CharField(max_lenght= 255)
    websites_count = models.CharField(max_lenght= 255)
    sources_count = models.CharField(max_lenght= 255)

    
    
    