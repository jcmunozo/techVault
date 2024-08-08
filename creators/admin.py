"""Creators Admin"""
# Django
from django.contrib import admin

# Import Export
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Creators
from .models import Creator

class CreatorResource(resources.ModelResource):
    class Meta:
        model = Creator

class CreatorAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name',)
    resources_class = CreatorResource

admin.site.register(Creator, CreatorAdmin)
