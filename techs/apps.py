"""Techs Apps"""
#django
from django.apps import AppConfig


class TechsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'techs'
    verbose_name = 'Techs'
