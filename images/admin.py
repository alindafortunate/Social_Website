from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Image


# Register your models here.
class ImageAdmin(ModelAdmin):
    list_display = ["title", "slug", "image", "created"]
    list_filter = ["created"]


admin.site.register(Image, ImageAdmin)
