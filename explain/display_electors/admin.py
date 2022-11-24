from django.contrib import admin

# Register your models here.

from .models import Territories, TerritoriesParents

admin.site.register(Territories)
admin.site.register(TerritoriesParents)