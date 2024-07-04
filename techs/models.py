from django.db import models
from django.contrib.auth.models import User

class Tech(models.Model):
    name = models.CharField(max_length=20)
    #image = models.ImageField()
    creator = models.CharField(max_length=40, blank=True)
    history = models.TextField(blank=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    documentation = models.URLField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Feature(models.Model):
    name = models.CharField(max_length=20)
    level = models.CharField(max_length=15)
    description = models.TextField()
    tech = models.ForeignKey(Tech, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' - ' + self.tech.name
