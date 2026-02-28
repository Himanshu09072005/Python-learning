class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, new_salary):
        if new_salary >= 0:
            self.__salary = new_salary
        else:
            print("Salary cannot be negative")