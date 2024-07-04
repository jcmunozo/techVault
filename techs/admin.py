from django.contrib import admin
from .models import Tech

class TechAdmin(admin.ModelAdmin):
    readonly_fields = ("created",)

admin.site.register(Tech, TechAdmin)
