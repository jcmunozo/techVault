"""Features Models"""
#django
from django.db import models
from django.contrib.auth.models import User

#libreries
from ckeditor.fields import RichTextField

#techs
from techs.models import Tech

class Feature(models.Model):
    class Level(models.TextChoices):
        BASIC = 'BASIC', 'Basic'
        INTERMEDIATE = 'INTERMEDIATE', 'Intermediate'
        ADVANCED = 'ADVANCED', 'Advanced'

    name = models.CharField("Feature name",max_length=20)
    level = models.CharField(max_length=12, choices=Level.choices, default=Level.BASIC,)
    description = RichTextField("Description")
    tech = models.ForeignKey(Tech, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField("Created", auto_now_add=True, blank=True)

    class Meta:
        verbose_name = 'Feature'
        verbose_name_plural = 'Features'

    def __str__(self):
        return self.name + ' - ' + self.tech.name
