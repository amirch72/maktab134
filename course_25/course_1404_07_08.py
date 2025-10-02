# requests
import requests
import json

ORIGIN_ADDRESS = "https://jsonplaceholder.typicode.com/"


def print_divider():
    print("----------------------------------------------------------------------")


def show_special_user(id):
    res = requests.get(f"{ORIGIN_ADDRESS}users/{id}")

    if res.status_code == 200:
        print_divider()
        print("Requested User")
        print_divider()
        print(res.text)
        print_divider()
    else:
        print("Your requeest failed")


def show_users():
    response = requests.get(f"{ORIGIN_ADDRESS}users")

    if response.status_code == 200:
        print_divider()
        print(f"username\t\tname\temail\tphone")
        print_divider()
        # response.json()
        # json.loads(response.text)
        for user in json.loads(response.text):
            print(
                f"{user["username"]}\t\t{user["name"]}\t{user["email"]}\t{user["phone"]}"
            )
            print_divider()
        print_divider()
        print_divider()
    else:
        print("Your requeest failed")


def add_new_user(**user_info):
    res = requests.post(f"{ORIGIN_ADDRESS}users", data=user_info)

    if res.status_code == 201:
        print_divider()
        print("Your user created!")
        print_divider()
        print(res.text)
        print_divider()
    else:
        print("Your requeest failed")


def edit_user(id, **new_info):
    res = requests.patch(f"{ORIGIN_ADDRESS}users/{id}", data=new_info)

    print(res.status_code)

    if res.status_code == 200:
        print_divider()
        print("Your requested user edited!")
        print_divider()
        print(res.text)
        print_divider()
    else:
        print("Your requeest failed")


# show_users()
# add_new_user(username="ali", name="Ali Ahmadi", email="ali@maktab.ir")
# show_special_user(5)


edit_user(5, name="Ali Hasani")


res = requests.delete(f"{ORIGIN_ADDRESS}users/3")
show_special_user(3)