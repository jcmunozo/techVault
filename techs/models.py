from django.utils.text import slugify
from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class Tech(models.Model):
    name = models.CharField("Name", max_length=20)
    creator = models.CharField("Creator", max_length=40, blank=True)
    history = RichTextField("History", blank=True)
    description = RichTextField("description")
    created = models.DateTimeField("Created", auto_now_add=True, blank=True)
    documentation = models.URLField("Documentation", max_length=50)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    slug = models.SlugField("slug", max_length=20)
    logo = models.ImageField("Logo",default='tech.png', blank=True)

    class Meta:
        verbose_name = 'Tech'
        verbose_name_plural = 'Techs'
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
