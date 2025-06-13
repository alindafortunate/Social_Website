from django.contrib.auth import get_user_model
from .models import Profile
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

    # Checking if passwords match.
    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError(
                "Passwords do not match, please ensure that they are mathcing."
            )
        return cd["password2"]

    # The above method will be executed upon calling is_valid() method.
    def clean_email(self):
        data = self.cleaned_data["email"]
        if get_user_model().objects.filter(email=data).exists():
            raise forms.ValidationError("Email already in use.")
        return data


class UserEditForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ["first_name", "last_name", "email"]

    def clean_email(self):
        data = self.cleaned_data["email"]
        qs = get_user_model().objects.filter(email=data).exclude(id=self.instance.id)
        if qs.exists():
            raise forms.ValidationError("Email already in use.")
        return data


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["date_of_birth", "location", "photo"]
