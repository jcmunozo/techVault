"""Techs Forms"""
# Django
from django import forms

# CKeditor 5
from django_ckeditor_5.widgets import CKEditor5Widget
from django_select2 import forms as s2forms

# Techs 
from . import models

class Create_new_tech(forms.ModelForm):
    """Techs model form"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["history"].required = False
    
    class Meta:
        """Form settings"""
        model = models.Tech
        fields = ('name','creator','history','description','documentation','logo', 'visibility')
        widgets = {
            'history':CKEditor5Widget(attrs={
                'class':'django_ckeditor_5',
                'placeholder': 'Enter the history of this tech'
            }, config_name='extends'),
            'creator': s2forms.Select2MultipleWidget(attrs={
                'class': 'form-control select2'
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter tech name'
            }),
            'logo': forms.ClearableFileInput(attrs={
                'class': 'form-control-file'
            }),
            'visibility': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Enter a brief description'
            }),
            'documentation': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter a valid URL'
            })
        }
