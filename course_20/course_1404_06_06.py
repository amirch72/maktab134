# def print_num(number: int) -> list[float]:
#     output = number * 9 / 10
#     return output


# print(print_num(23))


# name : str = "ali"

# print(name)


# def search_user(email: str) -> dict:
#     """
#         Prints the person's name and age.

#         If the argument 'additional' is passed, then it is appended after the main info.

#         Parameters
#         ----------
#         additional : str, optional
#             More info to be displayed (default is None)

#         Returns
#         -------
#         None
#     """
#     id: int = 10
#     pass
#     return {"first_name": "", "last_name": ""}

# global_var = 20


# def org_func():
#     org_var = "org var"
#     print(global_var)

#     def inner_func():
#         print(org_var)
#         inner_var = "inner var"
#         return inner_var


# print(global_var)


# def a(num):
#     global_var += num


# def b():
#     global_var /= 3


# def outer_fun():
#     var = "outer"
#     sum = 0

#     def inner_fun():
#         nonlocal var

#         var = "inner"
#         print("inner", var)

#     inner_fun()
#     print("outer", var)


# outer_fun()


# ------------------------------
import requests

res = requests.get(
    "https://jsonplaceholder.typicode.com/posts", params={"userId": 1, "id": 18}
)
print(res.status_code)
print(res.json())
print(res.headers["Date"])
# text, encoding, url

# res_patch = requests.patch(
#     "https://jsonplaceholder.typicode.com/users/2", data={"name": "Faghihe hasani"}
# )

# print(res_patch.json())

# res_post = requests.post(
#     "https://jsonplaceholder.typicode.com/users", {"name": "Tina Rostamkhani", "email": "test@maktab.ir"}
# )

# print(res_post.json())


# res_delete = requests.delete("https://jsonplaceholder.typicode.com/users/20")
# print(res_delete.json())


# -----------------------------------------------------
import json

my_dict = {"first_name": "Amirhossein", "last_name": "Chegounian"}
new_json = json.dumps(my_dict)

print(new_json, type(new_json))
converted_json = json.loads(new_json)
print(converted_json, type(converted_json))
