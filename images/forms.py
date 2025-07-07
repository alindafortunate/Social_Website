from django import forms
from .models import Image


class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ["title", "url", "description"]
        widgets = {"url": forms.HiddenInput}

    def clean_url(self):
        url = self.cleaned_data["url"]
        valid_extensions = ["jpg", "jpeg", "png"]
        extension = url.rsplit(".", 1)[1].lower()
        if extension not in valid_extensions:
            raise (
                "The given URL doesn't provided does not much valid image extension."
            )
        return url
