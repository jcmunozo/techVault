"""Features Forms"""
#django
from django import forms # difference between ModelForm and form

#ckeditor
from django_ckeditor_5.widgets import CKEditor5Widget

#features 
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
            'description':CKEditor5Widget(
                attrs={"class":"django_ckeditor_5"}, config_name="extends"
                ),
        }
