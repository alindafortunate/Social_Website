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
    def save(self, force_insert=False, force_update=False, commit=True):
        image = super().save(commit=False)
        image_url = self.cleaned_data["url"]

        return super().save(commit)

    # Today I didn't code I was in field.
    # The return to divine instructions.
