#ckeditor
from ckeditor.widgets import CKEditorWidget

#django
from django import forms # difference between ModelForm and form
#model 
from . import models

class Create_new_feature(forms.ModelForm):
    """Feature model form"""
    description = forms.CharField(widget=CKEditorWidget())
    
    class Meta:
        """Form settings"""

        model = models.Feature
        fields = ['name','level','description']
