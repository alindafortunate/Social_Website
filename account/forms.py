from django.contrib.auth import get_user_model
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat Password", widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ["username", "first_name", "last_name", "email"]
