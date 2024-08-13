"""Features Forms"""
# Django
from django import forms

# Ckeditor
from django_ckeditor_5.widgets import CKEditor5Widget

# Features 
from . import models

class Create_new_feature(forms.ModelForm):
    """Feature model form"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["description"].required = False

    class Meta:
        """Form settings"""

        model = models.Feature
        fields = ['name','level','description']
        widgets = {
            'description':CKEditor5Widget(attrs={
                'class':'django_ckeditor_5', 
                'placeholder':'Enter a description for this creator'
            }, config_name='extends'),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter creator name'
            }),
            'level': forms.Select(attrs={
                'class': 'form-select'
            })
        }
