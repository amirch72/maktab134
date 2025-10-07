class Person:
    def __init__(
        self,
        first_name="not submited",
        last_name="not submited",
        birthday=" not submited",
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday

    def data(self):
        print(
            f"the name is {self.first_name} and the lastName is {self.last_name} and the bd is {self.birthday}"
        )


class Teacher(Person):
    def __init__(
        self,
        first_name="not submited",
        last_name="not submited",
        birthday="not submited",
        personal_id="not registerd",

    ):
        self.id = personal_id
        super().__init__(first_name, last_name, birthday)
    
    def got_paid(self):
        print(f"mr {self.first_name} {self.last_name} got paid 10m")

    # def teacher_information(self, id):
    #     self.id = id


class Student(Person):
    def __init__(
        self,
        first_name="not submited",
        last_name="not submited",
        birthday=" not submited",
        student_id="not submited",
        entring="year",
        
    ):
        self.student_id = student_id
        self.year_of_entring = entring
        super().__init__(first_name, last_name, birthday)
    
    def paying(self):
        print(f"mr {self.first_name} {self.last_name} paid 10m ")

    


s1 = Student("ramin", "moahmmadi", "1382/07/02", 21, 1404)
a2 = Teacher("amir hossein", "cheguonian", "1372/11/21", 23)
# a= Teacher("user id")

# a2.teacher_information(23)
# print(a.first_name)
# print(b.first_name)
# print(a2.id)
# print(a2.first_name)
# print(a2.last_name)
# print(a2.birthday)

# print(s1.first_name)
# print(s1.last_name)
# print(s1.birthday)
# print(s1.student_id)
# print(s1.year_of_entring)
# s1.data()
# a2.data()
s1.paying()
a2.got_paid()
