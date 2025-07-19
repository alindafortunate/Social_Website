from django.urls import path
from .views import create_image

app_name = "images"

urlpatterns = [
    path("create/", create_image, name="create"),
]
