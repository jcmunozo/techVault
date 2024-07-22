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
    slug = models.SlugField("slug", unique=True, max_length=20)
    logo = models.ImageField("Logo",default='tech.png', blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created = models.DateTimeField("Created", auto_now_add=True, blank=True)
    creator = models.ManyToManyField(Creator)
    history = RichTextField("History", blank=True)
    visibility = models.BooleanField(default=False)
    description = RichTextField("description")
    documentation = models.URLField("Documentation", max_length=50)

    class Meta:
        ordering = ['name']
        verbose_name = 'Tech'
        verbose_name_plural = 'Techs'
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.generate_unique_slug()
        super().save(*args, **kwargs)

    def generate_unique_slug(self):
        slug = slugify(self.name.replace('+', 'plus').replace('#', 'sharp'))
        unique_slug = slug
        num = 1
        while Tech.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug
