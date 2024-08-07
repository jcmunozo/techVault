"""Creators Models"""
#django
from django.db import models
from django.contrib.auth.models import User

#libreries
from django_ckeditor_5.fields import CKEditor5Field

class Creator(models.Model):
    """Creators model"""
    name = models.CharField("Creator name",max_length=20)
    slug = models.SlugField("slug", unique=True, max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField("Created", auto_now_add=True, blank=True)
    biography = CKEditor5Field("Biography")

    class Meta:
        verbose_name = 'Creator'
        verbose_name_plural = 'Creators'

    def __str__(self):
       return self.name
