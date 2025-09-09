from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Action


@admin.register(Action)
class ActionAdmin(ModelAdmin):
    list_display = ["user", "verb", "target", "created"]
    list_filter = ["created"]
    search_fields = ["verb"]
