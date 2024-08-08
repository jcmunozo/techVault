"""Techs Admin"""
# Django
from django.contrib import admin

# Import Export
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Techs
from .models import Tech

class TechResource(resources.ModelResource):
    class Meta:
        model = Tech

class TechAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['name', 'creator']
    list_display = ('name', 'user')
    readonly_fields = ("created",)
    resources_class = TechResource


admin.site.register(Tech, TechAdmin)
