#django
from django.db import models
from django.contrib.auth.models import User

#model
from techs.models import Tech

class Feature(models.Model):
    name = models.CharField(max_length=20)
    level = models.CharField(max_length=15)
    description = models.TextField()
    tech = models.ForeignKey(Tech, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' - ' + self.tech.name
