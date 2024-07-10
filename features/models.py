#django
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

#model
from techs.models import Tech

class Feature(models.Model):
    name = models.CharField("Feature name",max_length=20)
    level = models.CharField("Feature's level",max_length=15)
    description = RichTextField("Description")
    tech = models.ForeignKey(Tech, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField("Created", auto_now_add=True, blank=True)

    class Meta:
        verbose_name = 'Feature'
        verbose_name_plural = 'Features'

    def __str__(self):
        return self.name + ' - ' + self.tech.name
