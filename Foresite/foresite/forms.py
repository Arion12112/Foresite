from django.contrib.auth.models import User
from django import forms


class SignUpForm(forms.ModelForm):
    username = forms.CharField(
        required=True,
        max_length=16,
        widget=forms.TextInput(
            attrs={
                'class': "input is-primary",
                'placeholder': "Username"
            }
        )
    )
    password = forms.CharField(
        required=True,
        max_length=16,
        widget=forms.PasswordInput(
            attrs={
                'class': "input is-primary",
                'placeholder': "Password"
            }
        )
    )

    class Meta:
        model = User
        fields = [
            'username',
            'password'
        ]
