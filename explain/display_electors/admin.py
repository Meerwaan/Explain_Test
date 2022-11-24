from django.contrib import admin

# Register your models here.

from .models import Territories, TerritoriesParents
admin.site.site_header = "Explain Admin"
admin.site.site_title = "Explain Admin"
admin.site.index_title = "Explain Admin"
admin.site.register(Territories)
admin.site.register(TerritoriesParents)
