# immutbale
# def test(name):
#     # name = "Ali Alavi"
#     name.capitilze()
#     return name


# x = "ali alavi"
# test(x)
# print(x)

# pure function
# c = 10

# def test2(a, b):
#     return (a + b) * c

# test2(2,51)
# print(test2(2, 5))


# side effect
# def test3(inp):
#     print(inp)

# test3("hello")

# lambda
# sum_num = lambda a, b: a + b
# print(sum_num(10,20))


# map
# student_score = [10, 12, 14, 8, 7, 13]
# student_info = [
#     {"name": "ali", "score": 14},
#     {"name": "mohsen", "score": 12},
#     {"name": "ariyan", "score": 8},
# ]

# output = []
# for i in student_score:
#     output.append(i * 1.4)

# print(output)


# def norm(number):
#     return number * 1.4


# print(list(map(norm, student_score)))
# print(list(map(lambda x: {"name": x["name"], "score": x["score"] * 1.4}, student_info)))


# filter
# print(list(filter(lambda x: x % 3 == 0, student_score)))

# for x in student_score:
#     if x % 3 == 0:


# reduce
from functools import reduce


# def test(x, y):
#     print(f"X: {x}\nY: {y}")
#     return x + y


# print(reduce(lambda x, y: x + y, student_score))

# y = 0
# for x in student_score:
#     y += x


# print(y)
# def test(x, y):
#     if x < y:
#         return x
#     return y


# print(reduce(test, student_score))
# print(reduce(lambda x, y: x if x > y else y, student_score))

# x = 10
# y = 20

# min_num = x if x < y else y
# print(min_num)


# generator
# def generator_example(n):
#     output = 1
#     i = 1
#     while i <= n:
#         output *= i
#         yield output
#         i += 1

# for i in generator_example(5):
#     print(i)

# # print(list(generator_example(3)))

# generator_example = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# generator_example = (x**2 for x in range(10))


# for i in generator_example:
#     print(i)
#     if i > 2:
#         break
# print("-------------------------------")
# for i in generator_example:
#     print(i)
#     if i > 5:
#         break
# print("-------------------------------")
# for i in generator_example:
#     print(i)

user_info = {"is_authenticated": False}


# def hello_world():
#     if user_info["is_authenticated"]:
#         print("Hello world")


# def login_required(func):
#     def wrapper():
#         if user_info["is_authenticated"]:
#             func()
#         else:
#             print("Please login first")

#     return wrapper

# import time


# def calc_time(func):
#     def wrapper():
#         beg_time = time.time()
#         output = func()
#         end_time = time.time()
#         print(end_time - beg_time)
#         return output

#     return wrapper


# # @login_required
# @calc_time
# def hello_world():
#     print("Hello world")
#     return "Hello world"


# output = hello_world()
# print(output)


# def factoriel(number):
#     if number > 0:
#         return number * factoriel(number - 1)
#     return 1


# print(factoriel(4))


# Set
# student_code = {"102894", "102578", "103848"}
# print(student_code)

# student_code.add("104579")
# print(student_code)

# student_code.update(["102489", "108156"])
# print(student_code)

# student_code.add("103848")
# print(student_code)

# for i in student_code:
#     print(i)


# print("-------------------------------------")
# while len(student_code) > 0:
#     print(student_code.pop())


# student_code.remove("545")
# student_code.discard("545")
# student_code.remove("103848")
# student_code.discard("103848")
# print(student_code)

# print(student_code.pop())
# print(student_code)

# student_code.clear()
# print(student_code)

# del student_code
# print(student_code)


# set1 = {1, 2, 3, 10, 20, 30, 45, 55, 65}
# set2 = {4, 5, 6, 40, 50, 60, 45, 55, 65}

# Union
# print(set1.update(set2))
# print(set1.union(set2))
# print(set1 | set2)

# Intersection
# print(set1.intersection(set2))
# print(set1 & set2)
# print(set1.intersection_update(set2))

# Difference
# print(set1 - set2)
# print(set2 - set1)
# print(set1.difference(set2))
# print(set1.difference_update(set2))

# symetric difference
# print(set1.symmetric_difference(set2))
# print(set1.symmetric_difference_update(set2))

# print("Set1: ", set1)
# print("Set2: ", set2)

from itertools import cycle

# for i in count(10,3):
#     print(i)
#     if i > 100:
#         break


# tes1 = [1, 2, 3, 4, 5]
# tes2 = (10, 15)

# print(list(chain(tes1, tes2)))


test = [1, 2, 3]

count = 1
for i in cycle(test):
    print(i)
    test.append(i * count)
    print(test)
    count += 1
    if count == 10:
        break


