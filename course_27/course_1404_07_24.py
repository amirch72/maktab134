VAL = 0.1


def hello(name):
    return f"hello {name}"


print(hello("ali"))


info_dict = {
    "first_name": "Zahra",
    "last_name": "Abbasi",
    "gender": "female",
}


def show_name():
    return f"{info_dict['first_name']} {info_dict['last_name']}"


print(show_name())


def cal_value(value):
    return value * VAL
