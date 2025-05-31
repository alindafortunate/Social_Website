from django.urls import path
from django.contrib.auth import views as auth_views

from .views import index, test_view

urlpatterns = [
    path("", index, name="home"),
    path("test/", test_view, name="test"),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
