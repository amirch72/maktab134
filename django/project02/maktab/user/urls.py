from django.urls import path
from .views import (
    add_user,
    test_view,
    show_users,
    show_user,
    login_view,
    logout_user,
)

urlpatterns = [
    path("add/", add_user, name="add-user"),
    path("show-all/", show_users, name="show-all-users"),
    path("show/<int:user_id>/", show_user, name="show-user"),
    path("test/", test_view, name="test"),
    path("login/", login_view, name="login-user"),
    path("logout/", logout_user, name="logout-user"),
]
