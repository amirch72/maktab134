from django import forms
from .models import MaktabUser
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = MaktabUser
        fields = [
            "first_name",
            "last_name",
            "email",
            "birthday",
            "gender",
        ]


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "username",
            "password",
        ]
