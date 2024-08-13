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
        fields = ['name','nationality','description','biography','picture']
        widgets = {
            'biography':CKEditor5Widget(
                attrs={"class":"django_ckeditor_5"}, config_name="extends"
                ),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter creator name'
            }),
            'picture': forms.ClearableFileInput(attrs={
                'class': 'form-control-file'
            }),
            'nationality': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter nationality'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Enter a brief description'
            }),
        }
