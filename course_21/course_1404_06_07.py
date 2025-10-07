#!/usr/bin/env python3

import argparse

student = [
    {
        "id": 1,
        "name": "majid",
        "lastname": "maleki",
        "age": 28,
        "gender": "male",
        "grade": 18,
    },
    {
        "id": 2,
        "name": "tina",
        "lastname": "rostamkhani",
        "age": 22,
        "gender": "female",
        "grade": 19,
    },
    {
        "id": 3,
        "name": "ramin",
        "lastname": "mohammadi",
        "age": 20,
        "gender": "male",
        "grade": 20,
    },
    {
        "id": 4,
        "name": "romina",
        "lastname": "mahmoud",
        "age": 22,
        "gender": "female",
        "grade": 18,
    },
]
# -m student with high grade
# --m two student with high frade
# get a new info to add to current dict


parser = argparse.ArgumentParser()
parser.add_argument("--male", action="store_true")
parser.add_argument("-g", "--grade", action="count", help="return grade student")
# parser.add_argument("name")
parser.add_argument("--adduser", action="extend", nargs="+")
args = parser.parse_args()

print(args.adduser)


def add_student(id, name, lastname, age, gender, grade):
    new_user = {
        "id": id,
        "name": name,
        "lastname": lastname,
        "age": age,
        "gender": gender,
        "grade": grade,
    }
    student.append(new_user)
    return new_user


if args.male:
    data = list(filter(lambda stu: stu["gender"] == "male", student))
    print(data)


if args.grade and args.grade > 0:
    student.sort(key=lambda x: x["grade"], reverse=True)

    print(student[: args.grade])


# if args.name:
#     data = list(filter(lambda stu: stu["name"] == args.name, student))
#     print(data)


if args.adduser:
    print(add_student(*args.adduser))


# search based on name based on id based on grade
