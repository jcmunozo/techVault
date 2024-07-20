"""Techs Models"""
#django
from django.utils.text import slugify
from django.db import models
from django.contrib.auth.models import User

#libreries
from ckeditor.fields import RichTextField

#creators
from creators.models import Creator

class Tech(models.Model):
    """Techs model"""
    name = models.CharField("Name", max_length=20)
    slug = models.SlugField("slug", max_length=20)
    logo = models.ImageField("Logo",default='tech.png', blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created = models.DateTimeField("Created", auto_now_add=True, blank=True)
    creator = models.ManyToManyField(Creator)
    history = RichTextField("History", blank=True)
    description = RichTextField("description")
    documentation = models.URLField("Documentation", max_length=50)

    class Meta:
        verbose_name = 'Tech'
        verbose_name_plural = 'Techs'
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
