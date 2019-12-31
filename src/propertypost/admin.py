from django.contrib.gis import admin
from .models import PropertyPost
from django.contrib.gis.admin import OSMGeoAdmin

class PropertyPostAdmin(OSMGeoAdmin):
    list_display = ['pk','type','viewnum','timestamp','updated']
    list_filter = ['type']
    ordering = ['-timestamp']
admin.site.register(PropertyPost, PropertyPostAdmin)