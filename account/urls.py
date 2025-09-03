from django.urls import path, include
from django.contrib.auth import views as auth_views

from .views import (
    index,
    test_view,
    dashboard,
    register,
    edit,
    list_users,
    user_detail,
    user_follow,
)

urlpatterns = [
    path("home/", index, name="home"),
    path("test/", test_view, name="test"),
    path("", dashboard, name="dashboard"),
    path(
        "", include("django.contrib.auth.urls")
    ),  # This code represents the below lines about authentication
    # path("login/", auth_views.LoginView.as_view(), name="login"),
    # path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    # path(
    #     "password_change/",
    #     auth_views.PasswordChangeView.as_view(),
    #     name="password_change",
    # ),
    # path(
    #     "password_change_done/",
    #     auth_views.PasswordChangeDoneView.as_view(),
    #     name="password_change_done",
    # ),
    # path(
    #     "password_reset/", auth_views.PasswordResetView.as_view(), name="password_reset"
    # ),
    # path(
    #     "password_reset_done/",
    #     auth_views.PasswordResetDoneView.as_view(),
    #     name="password_reset_done",
    # ),
    # path(
    #     "password_reset_confirm/<uidb64>/<token>/",
    #     auth_views.PasswordResetConfirmView.as_view(),
    #     name="password_reset_confirm",
    # ),
    # path(
    #     "password_reset_complete/",
    #     auth_views.PasswordResetCompleteView.as_view(),
    #     name="password_reset_complete",
    # ),
    path("register/", register, name="register"),
    path("edit/", edit, name="edit"),
    path("users/", list_users, name="user_list"),
    path("users/<username>/", user_detail, name="user_detail"),
    path("user/follow/", user_follow, name="user_follow"),
]
