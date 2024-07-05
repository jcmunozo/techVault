from django import forms # difference between ModelForm and form

class Create_new_tech(forms.Form):
    name = forms.CharField(label="Tech's name", max_length=200)
    slug = forms.SlugField(max_length=20)
