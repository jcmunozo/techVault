"""Creators Forms"""
# Django
from django import forms

# CKeditor 5
from django_ckeditor_5.widgets import CKEditor5Widget

# Creators
from . import models

class Create_new_creator(forms.ModelForm):
    """Creator model form"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["biography"].required = False

    class Meta:
        """Form settings"""

        model = models.Creator
        fields = ['name','picture','nationality','description','biography']
        widgets = {
            'biography':CKEditor5Widget(
                attrs={"class":"django_ckeditor_5"}, config_name="extends"
                ),
        }
