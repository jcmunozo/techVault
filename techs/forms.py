"""Techs Forms"""
# Django
from django import forms

# CKeditor 5
from django_ckeditor_5.widgets import CKEditor5Widget
from django_select2 import forms as s2forms

# Techs 
from . import models

class CreatorWidget(s2forms.ModelSelect2MultipleWidget):
    search_fields = [
        "name__icontains",
    ]

class Create_new_tech(forms.ModelForm):
    """Techs model form"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["description"].required = False
        self.fields["history"].required = False
    
    class Meta:
        """Form settings"""
        model = models.Tech
        fields = ('name','creator','history','description','documentation','logo', 'visibility')
        widgets = {
            'description':CKEditor5Widget(
                attrs={"class":"django_ckeditor_5"}, config_name="extends"
                ),
            'history':CKEditor5Widget(
                attrs={"class":"django_ckeditor_5"}, config_name="extends"
                ),
            'creator':CreatorWidget,
        }
