# class Public:
#     def __init__(self):
#         self.name = "John"

#     def display_name(self):
#         print(self.name)


# obj = Public()
# obj.display_name()
# print(obj.name)


# class Protected:
#     def __init__(self):
#         self._name = "John"


# class SubClass(Protected):
#     def display_name(self):
#         print(self._name)


# obj = SubClass()
# obj.display_name()
# print(obj._name)


# current_user = {
#     "name": "ali",
#     "username": "ali2"
# }

# class Private:
#     def __init__(self):
#         self.__salary = 2000


#     def salary(self):
#         if current_user["username"] == "ali":
#             return " ------ "
#         return f"{self.__salary}" + " $"


# obj = Private()
# # print(obj.__salary)
# print(obj.salary())


# current_user = {"username": "ali"}


# # Setter and Getter
# class Person:
#     def __init__(self, age):
#         # self.age = age
#         self.age_setter(age)

#     def age_setter(self, age):
#         if age > 0 and age < 150:
#             self._age = age
#         else:
#             print("Age is not valid")

#     def age_getter(self):
#         if current_user["username"] == "ali":
#             return "-----"
#         return self._age


# ali = Person(10)
# # print(ali._age)
# print(ali.age_getter())
# ali.age_setter(160)
# print(ali.age_getter())
# ali.age = 20


# class Person:
#     def __init__(self, age):
#         self.age = age

#     def age_setter(self, age):
#         if age > 0 and age < 150:
#             self._age = age
#         else:
#             print("Data is not valid")

#     def age_getter(self):
#         return self._age

#     age = property(age_getter, age_setter)


# class Person:
#     def __init__(self, rec_age):
#         self.age = rec_age

#     def __str__(self):
#         return f"This person has {self.age} old"

#     def __lt__(self, value):
#         if self.age < value.age:
#             return True
#         return False

#     # eq, ne, gt, lt, ge, le
#     def __ge__(self, value):
#         if self.age >= value.age:
#             return True
#         return False

#     def __eq__(self, value):
#         if self.age == value.age:
#             return True
#         return False

#     @property
#     def age(self):
#         return self._age

#     @age.setter
#     def age(self, rec_age):
#         if rec_age > 0 and rec_age < 150:
#             self._age = rec_age
#         else:
#             print("Data is not valid")
#             self._age = 0

#     @age.deleter
#     def age(self):
#         print("You have not permission")

#     # @age.deleter
#     # def age(self):
#     #     del self._age
#     #     print("Age deleted")


# majid = Person(21)
# ali = Person(21)
# del majid.age
# print(majid.age)


# print(majid >= ali)
# print(majid.__ge__(ali))


# class A:
#     def greet(self):
#         print("A")


# class B(A):
#     def greet(self):
#         print("B")


# class C(A):
#     def greet(self):
#         print("C")


# class D(C, B):
#     def greet(self):
#         print("D")


# obj = D()
# obj.greet()
# print(D.__mro__)


# class GreetMixin:
#     def greet(self):
#         print("Hiiii")


# class A(GreetMixin):
#     pass


# class B(A, GreetMixin):
#     pass


# class C(A, GreetMixin):
#     pass


# class D(C, B):
#     pass


# obj = D()
# obj.greet()


class Wheels:
    def __init__(self, num):
        self.number = num

    def fix(self):
        print("Fixed")


class Car:
    def __init__(self, wheels, name):
        self.wheels = wheels
        self.name = name


w = Wheels(4)
c = Car(w, "Pride")


print(c.wheels.number)
c.wheels.fix()
