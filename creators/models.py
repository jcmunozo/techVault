"""Creators Models"""
# Django
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# CKeditor 5
from django_ckeditor_5.fields import CKEditor5Field

class Creator(models.Model):
    """Creators model"""
    name = models.CharField("Creator name",max_length=30)
    slug = models.SlugField("slug", unique=True, max_length=35)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.ImageField("Creator picture",default='tech.png', blank=True)
    created = models.DateTimeField("Created", auto_now_add=True, blank=True)
    biography = CKEditor5Field("Biography")
    nationality = models.CharField("Creator nacionality", max_length=40, default="world")
    description = models.TextField("Creator description", default="tech creator")

    class Meta:
        verbose_name = 'Creator'
        verbose_name_plural = 'Creators'

    def __str__(self):
       return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Creator, self).save(*args, **kwargs)   

    def type_object(self):
        return 'Creator'
