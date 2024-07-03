from django.contrib import admin
from .models import Tech, Feature

class TechAdmin(admin.ModelAdmin):
    readonly_fields = ("created",)

admin.site.register(Tech, TechAdmin)
admin.site.register(Feature)
