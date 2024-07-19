"""Features Admin"""
#django
from django.contrib import admin

#libraries
from import_export import resources
from import_export.admin import ImportExportModelAdmin

#features
from .models import Feature

class FeatureResource(resources.ModelResource):
    class Meta:
        model = Feature

class FeatureAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['name', 'level']
    list_display = ('name', 'level',)
    resources_class = FeatureResource

admin.site.register(Feature, FeatureAdmin)
