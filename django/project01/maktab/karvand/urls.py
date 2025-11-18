from django.urls import path
from .views import show_karvand, create_mentors, update_mentors, delete_mentors

urlpatterns = [
    path("show/", show_karvand, name="show-karvands"),
    path("create/", create_mentors),
    path("update/", update_mentors),
    path("delete/", delete_mentors),
]
