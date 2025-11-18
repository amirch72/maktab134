from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm, LoginForm
from .models import MaktabUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


LOGIN_URL = "/user/login/"


# Create your views here.
def login_view(request):
    message = None
    form = LoginForm()

    if request.user.is_authenticated:
        return redirect("show-all-users")

    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        user = authenticate(
            request,
            username=username,
            password=password,
        )
        if user:
            login(request, user)
            return redirect("show-all-users")
        else:
            message = "Invalid username or password"
    else:
        message = "Welcome"

    return render(
        request,
        "login.html",
        {
            "form": form,
            "message": message,
        },
    )


def logout_user(request):
    logout(request)
    print(request.user)
    return redirect("login-user")

@login_required(
    login_url=LOGIN_URL,
    redirect_field_name="to",
)
def add_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show-all-users")
            # message = f"{form.cleaned_data['first_name']} {form.cleaned_data['last_name']} created!"
            # form = UserForm()
            # return render(request, "add-user.html", {"form": form, "message": message})
    else:
        form = UserForm()
    return render(request, "add-user.html", {"form": form})


@login_required(
    login_url=LOGIN_URL,
    redirect_field_name="to",
)
def show_users(request):
    all_users = MaktabUser.objects.all()
    return render(
        request,
        "show-users.html",
        {"data": all_users},
    )


@login_required(
    login_url=LOGIN_URL,
    redirect_field_name="to",
)
def show_user(request, user_id):
    try:

        requested_user = MaktabUser.objects.get(id=int(user_id))
        return render(request, "show-user.html", {"user": requested_user})
    except:
        return HttpResponse("Error")


def test_view(request):
    # reza_gholami = MaktabUser.objects.get(id=3)
    # reza_gholami.deleted = True
    # reza_gholami.save()
    # print(reza_gholami)
    not_deleted_user = MaktabUser.objects.all()
    for user in not_deleted_user:
        print(user)

    print("-" * 20)
    all_users = MaktabUser.objects.archive()
    for user in all_users:
        print(user)

    print("-" * 20)
    MaktabUser.objects.test()
    deleted_users = MaktabUser.objects.deleted_records()
    for user in deleted_users:
        print(user)
    return render(request, "test.html")
