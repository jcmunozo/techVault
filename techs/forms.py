"""Techs Forms"""
#django
from django import forms

#libreries
from django_ckeditor_5.widgets import CKEditor5Widget

#techs 
from . import models

class Create_new_tech(forms.ModelForm):
    """Techs model form"""
    
    class Meta:
        """Form settings"""
        model = models.Tech
        fields = ('name','creator','history','description','documentation','logo', 'visibility')
        widgets = {
            'description':CKEditor5Widget(
                attrs={"class":"django_ckeditor_5"}, config_name="comment"
                ),
            'creator':forms.SelectMultiple()
        }
