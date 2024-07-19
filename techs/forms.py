"""Techs Forms"""
#django
from django import forms

#techs 
from . import models

class Create_new_tech(forms.ModelForm):
    """Techs model form"""

    class Meta:
        """Form settings"""
        model = models.Tech
        fields = ('name','creator','history','description','documentation','logo')
