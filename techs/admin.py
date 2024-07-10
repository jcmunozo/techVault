from django.contrib import admin
from .models import Tech
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class TechResource(resources.ModelResource):
    class Meta:
        model = Tech

class TechAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['name', 'creator']
    list_display = ('name', 'creator',)
    readonly_fields = ("created",)
    resources_class = TechResource


admin.site.register(Tech, TechAdmin)
