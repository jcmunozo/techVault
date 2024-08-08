"""Features Models"""
# Django
from django.db import models
from django.contrib.auth.models import User

# Libreries
from django_ckeditor_5.fields import CKEditor5Field

# Techs
from techs.models import Tech

class Feature(models.Model):
    """Feature model"""
    class Level(models.TextChoices):
        BASIC = 'BASIC', 'Basic'
        INTERMEDIATE = 'INTERMEDIATE', 'Intermediate'
        ADVANCED = 'ADVANCED', 'Advanced'

    name = models.CharField("Feature name",max_length=20)
    tech = models.ForeignKey(Tech, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    level = models.CharField(max_length=12, choices=Level.choices, default=Level.BASIC,)
    created = models.DateTimeField("Created", auto_now_add=True, blank=True)
    description = CKEditor5Field("Description", config_name='extends')

    class Meta:
        verbose_name = 'Feature'
        verbose_name_plural = 'Features'

    def __str__(self):
        return self.name + ' - ' + self.tech.name
