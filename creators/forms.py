"""Creators Forms"""
#ckeditor
from ckeditor.widgets import CKEditorWidget

#django
from django import forms # difference between ModelForm and form

#creators
from . import models

class Create_new_creator(forms.ModelForm):
    """Creator model form"""
    biography = forms.CharField(widget=CKEditorWidget())
    
    class Meta:
        """Form settings"""

        model = models.Creator
        fields = ['name','biography']
