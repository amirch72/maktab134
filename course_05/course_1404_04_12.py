# x = "10"

# if x:
#     print("hello")

# a = 10
# b = 20
# c = 15
# score_ali = 10.5
# score_atefe = 18

# # List
# # score_of_students = [10, 20, 30, 50, 15, 65]
# # print(score_of_students)
# # score_of_students[5] = 30
# # print(score_of_students)
# # # Tuple
# # score_of_students_tuple = (10, 20, 30, 50, 15, 65)
# # # Set
# # score_of_students_set = {10, 20, 30, 50, 15, 65}
# # print(type(score_of_students_set))
# # Dictionary -> key-value
# ali_info = {"name": "Ali", "age": 23, "phone": "021345678900"}

# print("--------- First info of ali ---------")
# print(ali_info)

# # atefe_info = dict(name="Atefe", age=25)
# # print(atefe_info)

# ali_info_list = ["Ali", 23]


# ali_info["phone"]

# # print(ali_info["phones"])
# # print(ali_info.get("names", "Student"))

# # ali_info["phone"] = "09123456789"
# # print("--------- Update phone ---------")
# # print(ali_info)

# # ali_info.update({"age": 27})
# # print("--------- Update age ---------")
# # print(ali_info)


# # ali_info["last_name"] = "madani"
# # print("--------- Update|Add last_name ---------")
# # print(ali_info)

# # ali_info.update({"grade": 19.5})
# # print("--------- Update|Add grade ---------")
# # print(ali_info)

# # ali_info.popitem()
# # print("--------- Use from popitem ---------")
# # print(ali_info)

# # # ali_info.pop("phone")
# # # del ali_info["phone"]
# # print("--------- Use from pop|del ---------")
# # # del ali_info
# # ali_info.clear()
# # print(ali_info)


# # ali_info_copy = ali_info

# # ali_info_copy = {"new": "new"}
# # ali_info["name"] = "Ali asghar"

# ali_info_copy = dict(ali_info)
# ali_info_copy_2 = ali_info.copy()

# ali_info_copy["age"] = 25
# ali_info_copy_2["name"] = "Aliiii"

# print("Copy2: ", ali_info_copy_2)
# print("Copy: ", ali_info_copy)
# print("Origin: ", ali_info)

# print(ali_info.items())     # return all key-value pairs
# print(ali_info.values())    # return all values
# print(ali_info.keys())      # return all keys

# for i,j in ali_info.items():
#     print(i,j)

# # rgb = ["", "", ""]
# # rgba = list(rgb)
# # rgba.append("")

# # print(rgb)
# # print(rgba)


# # x = 10
# # y = x

# # y = 20

# # print(f"x: {x}\ny: {y}")


# if ali_info["age"] > 100:
#     print("hello")

# if "name" in ali_info:
#     print(f"Hello {ali_info["name"]}")
# else:
#     print("Hi")


# scores_of_students = (10.5, 15, 19, 10, 2, 9, 20)
# # scores_of_students[0] = 20 -> Error
# converted_scores = list(scores_of_students)
# print(converted_scores)
# converted_scores[0] = 20
# print(converted_scores)

# print(scores_of_students[2], "\n\n\n")

# for i in scores_of_students:
#     print(i)


# colors = ("green", "red", "blue", "red")
# print(colors)

# # (gr, re, bl) = colors
# # print(gr, re)


# new_colors = colors * 2
# print(new_colors)

# print(new_colors.count("blue"))
# if "greens" in new_colors:
#     print(new_colors.index("green"))


# ///////////////////////////////////////////////////////////////////
new_list = [1, 2, 3, 4, 5, 6, [4, 5, 6], 7, 8, 9]
print(new_list)
copied_list = [sum(i) for i in new_list if type(i) != int]
print(copied_list)
# new_list = ["1", "2"]

# copies_list = [str(i) * 10 for i in new_list]
# new_string = "".join(copies_list)
# print(new_string)


# new_string = "Ali"
# print(new_string.capitalize())
# print(new_string.lower())
# print(new_string.upper())


# if new_string.lower() == "ali".lower():
#     print("Hello")

# print(new_list)
# print("".join(new_list))

# //////////////////////////////////////////////////////////
# new_string = "Hello World"
# print(new_string.lower())
# print(new_string.upper())
# print(new_string.capitalize())
# if new_string.upper().isupper():
#     print("hi")

# new_string_2 = "123"
# if new_string_2.isnumeric():
#     print("is numeric")

# print("hello world".replace(" ", "").isalpha())
# if new_string.isalpha():
#     print("Yes")

# password = "@li"
# username = "ali"

# input_username = "AlI"
# input_password = "Ali"

# # a -> @ | s -> $

# if username.lower() == input_username.lower():
#     if password == input_password.replace("a", "@").replace("s", "$"):
#         print("Welcome")
#     else:
#         print("Password is wrong")
# else:
#     print("Input username is not exist")


# txt = "Hi {name} {last_name}"
# print(txt.format(name="ali", last_name="Mohseni"))

# number = 50

# print(f"{number:04d}")

# COPY ///////////////////////////////////////////////
# import copy

# new_list = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]

# copy_list = copy.deepcopy(new_list)

# # copy_list[1] = 20
# copy_list[1][1] = 20

# print("Origin: ", new_list)
# print("Copy: ", copy_list)


# nested ////////////////////////////////////////////////
ali_info = {
    "address": {"Country": "Iran", "Province": "Tehran"},
    "age": 23,
    "name": "Ali",
    "contact": {"email": "ali@gmail.com", "phone": ["02134567890", "09123456789"]},
}

print(ali_info["contact"]["phone"][0])
# print(ali_info["contact"]["email"])

student_info = [
    {
        "address": {"Country": "Iran", "Province": "Tehran"},
        "age": 23,
        "name": "Ali",
        "contact": {"email": "ali@gmail.com", "phone": ["02134567890", "09123456789"]},
    },
    {
        "address": {"Country": "Iran", "Province": "Tehran"},
        "age": 23,
        "name": "Ali",
        "contact": {"email": "ali@gmail.com", "phone": ["02134567890", "09123456789"]},
    },
]
for stu in student_info:
    print(stu["name"], stu["age"], stu["contact"])

new_list = [
    [1, 2, 3],
    [4, 5, 6],
    {"email": "ali@gmail.com", "phone": ["02134567890", "09123456789"]},
]

print(new_list)


new_list = "hello world ali".split(" ")
cap_str = [i.capitalize() for i in new_list]
print(cap_str)
print(" ".join(cap_str))

# print(" ".join("hello world".split(" ").capitalize()))
