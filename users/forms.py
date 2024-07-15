from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            'required':'True',
            'name':'username',
            'type':'text',
            'placeholder':'username',
            'maxlength':'16',
            'minlength':'6'
        })
        self.fields["email"].widget.attrs.update({
            'required':'True',
            'name':'email',
            'type':'email',
            'placeholder':'example@dev.co',
        })
        self.fields["password1"].widget.attrs.update({
            'required':'True',
            'name':'password1',
            'type':'password',
            'placeholder':'password',
        })
        self.fields["password2"].widget.attrs.update({
            'required':'True',
            'name':'password1',
            'type':'password',
            'placeholder':'password',
        })

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
