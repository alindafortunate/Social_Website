from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import LoginForm


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
    print(request.user.get_username())
    return render(request, "account/dashboard.html", {"section": "dashboard"})
