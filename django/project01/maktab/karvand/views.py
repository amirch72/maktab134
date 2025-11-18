from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Mentors

# Create your views here.

rec_data = {
    "first_name": "Reza",
    "last_name": "Yadegari",
    "username": "reza_yadegari",
    "gender": True,
    "email": "yadegari@maktab134.com",
}


def show_karvand(request):
    # Select * from mentors where id=3;
    special_user = Mentors.objects.all()
    print(special_user)
    for i in special_user:
        print(i.first_name)
    # Select * from mentors;
    # all_mentors = Mentors.objects.all()
    # for mentor in all_mentors:
    #     print(mentor.first_name, mentor.last_name, mentor.username)
    # return HttpResponse(f"Hello {special_user.first_name} {special_user.last_name}")
    return HttpResponse("Hi")


def create_mentors(request):
    try:
        new_mentor = Mentors(**rec_data)
        new_mentor.save()
        return HttpResponse("Created!")
    except:
        return HttpResponse("Error")


def update_mentors(request):
    try:
        # Received data from user
        rec_id = 3
        name = "Yas"
        # -----------------------

        requested_mentor = Mentors.objects.get(id=rec_id)
        requested_mentor.first_name = name
        requested_mentor.save()
        return HttpResponse("Updated!")
    except:
        return HttpResponse("Error")


def delete_mentors(request):
    try:
        # Received data from user
        rec_id = 4
        # -----------------------

        requested_mentor = Mentors.objects.get(id=rec_id)
        requested_mentor.delete()
        return HttpResponse("Deleted!")
    except:
        return HttpResponse("Error")