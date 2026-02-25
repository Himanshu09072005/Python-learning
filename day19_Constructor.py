class Student:

    def __init__(self, name, age):

        # instance variables
        self.name = name
        self.age = age

    def show(self):
        print("Name:", self.name)
        print("Age:", self.age)


s1 = Student("Himanshu", 18)
s2 = Student("Rahul", 20)

s1.show()
s2.show()