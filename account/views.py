from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd["username"], password=cd["password"])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("Authenticated successfully")
                else:
                    return HttpResponse("Disabled account.")
            else:
                return HttpResponse("Invalid login details.")
    else:
        form = LoginForm()
    return render(request, "account/login.html", {"form": form})


@login_required
def index(request):
    return render(request, "account/home.html")


@login_required
def test_view(request):
    return HttpResponse("Test was successful.")


@login_required
def dashboard(request):
    return render(request, "account/dashboard.html", {"section": "dashboard"})


def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but wait to save it yet because you have to set it's password.
            new_user = user_form.save(commit=False)
            # Set it's password.
            new_user.set_password(user_form.cleaned_data["password"])
            # Then save it to the database.
            new_user.save()
            Profile.objects.create(user=new_user)
            messages.success(request, "Account creation was successful.")
            return render(request, "account/register_done.html", {"new_user": new_user})

        else:
            messages.error(
                request,
                "Error, account creation was not successful please cross check the fields.",
            )
    else:
        user_form = UserRegistrationForm()

    return render(request, "account/register.html", {"user_form": user_form})


@login_required
def edit(request):
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(
            instance=request.user.profile, data=request.POST, files=request.FILES
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "User Profile Update was successful, thank you.")
        else:
            messages.error(
                request, "Error, User Profile Update failed, cross check the fields."
            )
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(
        request,
        "account/edit.html",
        {"user_form": user_form, "profile_form": profile_form},
    )


# On 11th/June/2025 I didn't code because I was supposed to go to field and I stopped past Wabigalo.
# On this very day I chose to surrender more to the Lord Jesus and His supreme authority over my life.

# On this day, I was caught up with Building Tomorrow work, so I didn't code.
# On this day I was in for a training of social entrepreneurship with Building Tomorrow.
# This day too I was in the training of Building Tomorrow.
# This day too I was preparing for the pitc presentation during the Building Tomorrow Training.
# On this day I was still trying to harmonise the content of Front-End and relaxing.

# Returning to Backend Programming.
# On this day I was not feeling well and was preparing for something.
# On this day I was still not able to program due to some difficulties.

# On 20th/Aug/2025, I retirned to Software Development after first dropping the ALX Course about Front-End to first read and complete the book about Django (Django-5-By-Example)