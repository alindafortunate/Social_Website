from django.urls import path
from .views import create_image, image_detail, image_like

app_name = "images"

urlpatterns = [
    path("create/", create_image, name="create"),
    path("detail/<int:id>/<slug:slug>/", image_detail, name="detail"),
    path("like/", image_like, name="like"),
]
