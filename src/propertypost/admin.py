from django.contrib import admin
from .models import PropertyPost



class PropertyPostAdmin(admin.ModelAdmin):
    list_display = ['pk','type','viewnum','timestamp','updated']
    list_filter = ['type']
    ordering = ['-timestamp']
admin.site.register(PropertyPost, PropertyPostAdmin)