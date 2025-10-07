from abc import ABC, abstractmethod


class DiscountMixin:
    def print_discount(self, mount, dis_type=None):
        if dis_type:
            print(
                f"{self.id}-{self.name} price with discount is: {self.discount(mount, dis_type)}$"
            )
        else:
            print(
                f"{self.id}-{self.name} price with discount is: {self.discount(mount)}$"
            )

    # def print_discount(self, mount):
    #     print(f"{self.id}-{self.name} price with discount is: {self.discount(mount)}$")


class Product(ABC):
    uuid = 0

    def __init__(self, category, price, name=""):
        Product.uuid += 1
        self.id = Product.uuid
        self.name = name
        self.category = category
        self.price = price

    def show_info(self):
        print("\n\n------------------ SHOW INFO ------------------")
        print(
            f"ID: {self.id}\nName: {self.name}\nCategory: {self.category}\nPrice: {self.price}$"
        )

    @abstractmethod
    def discount(self):
        pass


class Mobile(Product, DiscountMixin):

    def __init__(self, name, price, ram, cpu, hard, type):
        super().__init__("Digital > Mobile", price, name)
        self.ram = ram
        self.cpu = cpu
        self.hard = hard
        self.type = type
        self.basic = {
            "editable": True,
            "deletable": False,
            "exist": True,
            "deleted": False,
        }

    def show_info(self):
        super().show_info()
        print(f"Ram: {self.ram}\nCPU: {self.cpu}\nType: {self.type}")

    def discount(self, discount_mount, discount_type="percent"):
        if discount_type == "percent":
            if discount_mount > 5 and discount_mount <= 50:
                return self.price * (100 - discount_mount) / 100
            else:
                raise ValueError("Invalid discount mount. (5 < x <= 50)")
                # print("Invalid discount mount. (5 < x <= 50)")
        elif discount_type == "price":
            if self.price > discount_mount:
                return self.price - discount_mount
            else:
                print("Invalid discount mount. (discount < price)")
        else:
            print("Invalid discount")

        return -1


class Book(Product, DiscountMixin):
    def __init__(self, name, price, subject):
        super().__init__("Book", price, name)
        self.subject = subject

    def discount(self, discount_mount):
        if discount_mount > 5 and discount_mount <= 50:
            return self.price * (100 - discount_mount) / 100

        print("Invalid discount mount. (5 < x <= 50)")
        return -1


# p1 = Product("Digital", "12000", "Mobile")
# p1.show_info()
m1 = Mobile("Redmi 12", 130, 8, "", 128, "Android")
m2 = Mobile("Redmi 13", 160, 8, "", 128, "Android")
# m1.show_info()
# p2 = Product("Book", "2", "Farsi 2")
# p2.show_info()
b1 = Book("Oloom 2", 3, "Darsi")
# b1.show_info()

# print(b1.discount(50))

# print(m1.discount(35))
# m1.print_discount(60)
# m1.print_discount(30, "price")
# b1.print_discount(45)
# all_mobile = [m1, m2]
# new_dict = {i.id: i.id * i.id for i in all_mobile if i.id != 3}
# print(new_dict)
# print(new_dict[2])
# print([{i.id: i.name} for i in all_mobile])


# -----------------------------------------
new_person = {
    "first_name": "ali",
    "last_name": "alavi",
    "address": {
        "country": "iran",
        "province": "tehran",
        "city": "tehran",
        "sub_address": "st.",
    },
}


# print(new_person)
print(new_person["first_name"])
print(new_person["last_name"])
# print(new_person["address"])
print(new_person["address"]["country"])
print(new_person["address"]["province"])
print(new_person["address"]["city"])

# new_person["phone"] = "09123456789"
new_person["phone"] = {}
new_person["phone"]["work"] = "09123456789"
new_person["phone"]["home"] = "09123356789"
print(new_person["phone"])
del new_person["phone"]["home"]
print(new_person["phone"])


for i, j in new_person.items():
    if isinstance(j, dict):
        print(i, " ----------")
        for ii, jj in j.items():
            print(ii, jj)
    else:
        print(i, j)



new_person["deletable"] = False

if "deleted" in new_person:
    # return
    del new_person["deleted"]