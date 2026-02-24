class Student:

    def set_data(self, name, age):
        self.name = name
        self.age = age

    def show_data(self):
        print("Name:", self.name)
        print("Age:", self.age)


s1 = Student()
s2 = Student()

s1.set_data("Himanshu", 18)
s2.set_data("Rahul", 20)

s1.show_data()
s2.show_data()