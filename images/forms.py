import requests
from django.core.files.base import ContentFile
from django.utils.text import slugify
from django import forms
from .models import Image


class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ["title", "url", "description"]
        widgets = {"url": forms.HiddenInput}

    def clean_url(self):
        url = self.cleaned_data["url"]
        common_extentions = ["jpg", "jpeg", "png"]
        extention = url.rsplit(".", 1)[1].lower()
        if extention not in common_extentions:
            raise forms.ValidationError(
                "The given url doesn't much valid image extentions."
            )
        return url

    # Today I didn't code.
    # Today I didn't code as well.
    # force_insert=False, force_update=False,
    def save(self, force_insert=False, force_update=False, commit=True):
        image = super().save(commit=False)
        image_url = self.cleaned_data["url"]
        extension = image_url.rsplit(".", 1)[1].lower()
        name = slugify(image.title)
        image_name = f"{name}.{extension}"
        # Dowload the image from the given URL.
        response = requests.get(image_url)
        image.image.save(image_name, ContentFile(response.content), save=False)
        if commit:
            image.save()
        return image

    # Today I didn't code I was in field.
    # The return to divine instructions.
