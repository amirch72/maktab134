from django.db import models

# Create your models here.
# class ddddddddd():
#     field = dfdfsdf


class Mentors(models.Model):
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField()
    birthday = models.DateField(null=True)
    date_register = models.DateTimeField(auto_now_add=True)
    gender = models.BooleanField()
    username = models.CharField(default="test")
    email = models.EmailField(default="test@test.com")


class Students(models.Model):
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField()
    birthday = models.DateField()
    date_register = models.DateTimeField(auto_now_add=True)
    gender = models.BooleanField()
    username = models.CharField()
    email = models.EmailField()
