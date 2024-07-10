"""Post Tech's"""

#django
from django import forms # difference between ModelForm and form

#model 
from . import models

class Create_new_tech(forms.ModelForm):
    """Tech's model form"""

    class Meta:
        """Form settings"""
        model = models.Tech
        fields = ('name','creator','history','description','documentation','logo')
