from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Profile


class ProfileAdmin(ModelAdmin):
    list_display = ["user", "date_of_birth", "photo", "location"]
    raw_id_fields = ["user"]


admin.site.register(Profile, ProfileAdmin)
