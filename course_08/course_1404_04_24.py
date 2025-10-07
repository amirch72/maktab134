class Car:
    count = 0

    def __init__(self, n="Pride", c="White", d=4):
        self.name = n
        self.color = c
        self.door = d
        Car.count += 1
        print("Created")

    @classmethod
    def count_of_cars(cls):
        print(cls.count)

    def start(self):
        print(f"Start {self.name} ....")

    @staticmethod
    def compare(c1, c2):
        if c1.door > c2.door:
            print(f"{c1.name} is great")
        else:
            print(f"{c2.name} is great")

    @staticmethod
    def print_car():
        print("This is car class")


class HighLux:
    pass


class Benz(Car, HighLux):
    def __init__(self, c="White"):
        self.auto = False
        super().__init__("Benz", c, 2)

    def start(self):
        print(f"Start {self.name} quietly....")

    def auto_drive(self):
        self.auto = not self.auto
        if self.auto:
            print("Auto dirve is active")
        else:
            print("Auto dirve is deactive")


class NewGenBenz(Benz):
    pass


# class NewGenBenz:
#     count = 0

#     def __init__(self, c="White"):
#         self.auto = False
#         super().__init__("Benz", c, 2)

#     @classmethod
#     def count_of_cars(cls):
#         print(cls.count)

#     def start(self):
#         print(f"Start {self.name} quietly....")

#     @staticmethod
#     def compare(c1, c2):
#         if c1.door > c2.door:
#             print(f"{c1.name} is great")
#         else:
#             print(f"{c2.name} is great")

#     @staticmethod
#     def print_car():
#         print("This is car class")


#     def auto_drive(self):
#         self.auto = not self.auto
#         if self.auto:
#             print("Auto dirve is active")
#         else:
#             print("Auto dirve is deactive")


Car.print_car()
# def compare(c1, c2):
#     if c1.door > c2.door:
#         print(f"{c1.name} is great")
#     else:
#         print(f"{c2.name} is great")


# class method
# instance method
# static method

b_1 = Benz("Blue")
b_2 = Benz("White")

b_1.print_car()

b_1.compare(b_1, b_2)

print("Benz name: ", b_1.name)
b_1.start()
b_1.auto_drive()
b_1.auto_drive()
b_1.auto_drive()
b_1.auto_drive()

a_1 = Car("Peykan", "Black", 6)
# a_1.name = "Peykan"
a_2 = Car()
# a_2.name = "Pride"

Car.compare(a_1, a_2)


# a_2.color = "white"

print(a_1.door)
print(a_1.color)

print(a_2.door)
print(a_2.color)


a_1.start()
# a_1.count = 20
print(a_1.count)
# start(a_1)
Car.count_of_cars()
# count_of_cars(Car)

# print(Car.name)
