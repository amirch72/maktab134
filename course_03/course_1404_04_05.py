from new_module import (
    calc,
    for_example,
    print_hello as p_hello,
    print_hello_to_all_new_student_and_register as hello_and_register,
)
import sys
import numpy

# sys.path.append("/home/chegouniyan/Desktop/maktab_sharif/134/course_01")
# import course_1404_03_22


def print_hello():
    print("Hello world")


def sum_num(a, b, mul=1, div=1):
    return ((a + b) * mul) / div


print(sum_num(10,30, div=3))

def sum_multi_num(*args):
    # print(args)
    # output = 0
    # for i in args:
    #     output += i
    # return output
    return sum(args)


def hello_student_arg(*args):
    for i in args:
        print(f"Hello {i}")

# hello_student_arg("Ali", "Maryam", "Ariyan", "Mohmmad amin", "Atefe")
# print(sum_multi_num(1, 2, 4, 5))


# print(calc(10, 20))
# print(calc(10, 20, "+"))
# print(calc(10, 20, "-"))
# print(calc(10, 0, "/"))
# print(calc(10, 20, "*"))
# print(calc(10, 20, "6666"))

# print(for_example())


def hello_student(student="jkdsfjdsjhb"):
    print(f"Hello {student}")


# print_hello()

# print(type(sum_num(30, 15)))
# x = sum_num(10, 20)
# print(x)

# print(student)
ss = "Ali"
ali = "Ali"
# hello_student(344534)
# hello_student(ali)
# hello_student()
# print(hello_student())
# num_1 = int(input("Number 1: "))
# num_2 = int(input("Number 2: "))

# output = sum_num(num_1, num_2)


def average_list(*nums):
    return sum(nums) / len(nums)

lst = [12,13,14,15]
print(f"average is {average_list(12,13,14,15)}")

