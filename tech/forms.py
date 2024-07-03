from django import forms # difference between ModelForm and form

class Create_new_feature(forms.Form):
    name = forms.CharField(label="Feature's name", max_length=100)
    description = forms.CharField(label="description", widget=forms.Textarea)

class Create_new_tech(forms.Form):
    name = forms.CharField(label="Tech's name", max_length=200)
