# print(10/0)
# try:
#     print(10/0)
# except:
#     print("Zero Deivision Error")

# print("Hello")

lst = [10,0]

# try:
#     print(lst[0]/lst[2])
# # except IndexError:
# #     print("Index error")
# # except ZeroDivisionError:
# #     print("Zero division")
# except:
#     print("Wrong")
# else:
#     print("Correct")
# finally:
#     print("Both")

# print("Both")

# username = "Ali2"

# assert username != "Ali", "Bad request"
# # if username == "Ali":
# #     raise NameError("Bad request")
# try:
#     if username == "Ali":
#         raise Exception("Bad request")
#     # assert username != "Ali", "Bad request"
#     print("Welcome to my site")
# except Exception as e:
#     print(e)


# f = open("course_04/test.txt")
# print(f.read())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# file_lines = f.readlines()
# for line in file_lines:
#     print(line)
#     words = line.split(" ")
#     print(words)
#     for word in words:
#         print(word)

f = open("course_04/test.txt", "wt")

f.write("\nHello world")
# f.close()

ff = open("course_04/test.txt", "rt")
print(ff.read())

my_string = "Hello world"

with open("course_04/test.txt", "at") as f:
    print("Hi guys", file=f)
    print(my_string.encode(encoding="utf-8",errors="replace"), file=f)


# print("10", 20 ,30 ,40, sep=" | ", end=" /// ")
# print("10", 20 ,30 ,40, sep=" | ", end=" /// ")

# my_string = "Hello world"
# print(my_string.encode(encoding="utf-8",errors="replace"))

print(bin(8))
print(hex(5454))
print(oct(7))

print(int(0x154e))

"10 a 11 b 12 c 13 d 14 e 15 f"