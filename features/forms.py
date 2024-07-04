from django import forms # difference between ModelForm and form

class Create_new_feature(forms.Form):
    name = forms.CharField(label="Feature's name", max_length=100)
    description = forms.CharField(label="description", widget=forms.Textarea)
