#django
from django import forms # difference between ModelForm and form
#model 
from . import models

class Create_new_feature(forms.ModelForm):
    """Feature model form"""
    class Meta:
        """Form settings"""

        model = models.Feature
        fields = ['name','level','description']
