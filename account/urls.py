from django.urls import path
from django.contrib.auth.views import LoginView

from .views import index

urlpatterns = [
    path("", index, name="home"),
    path("login/", LoginView.as_view(), name="login"),
]
