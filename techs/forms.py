"""Techs Forms"""
#django
from django import forms

#ckeditor
from ckeditor.widgets import CKEditorWidget

#techs 
from . import models

class Create_new_tech(forms.ModelForm):
    """Techs model form"""
    description = forms.CharField(widget=CKEditorWidget())
    
    class Meta:
        """Form settings"""
        model = models.Tech
        fields = ('name','creator','history','description','documentation','logo')
        widgets = {
            'creator':forms.SelectMultiple()
        }
