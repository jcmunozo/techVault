"""Creators Forms"""
#django
from django import forms # difference between ModelForm and form

#libreries
from django_ckeditor_5.widgets import CKEditor5Widget

#creators
from . import models

class Create_new_creator(forms.ModelForm):
    """Creator model form"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["biography"].required = False

    class Meta:
        """Form settings"""

        model = models.Creator
        fields = ['name','biography']
        widgets = {
            'biography':CKEditor5Widget(
                attrs={"class":"django_ckeditor_5"}, config_name="extends"
                ),
        }
