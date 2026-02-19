FILENAME = "students.txt"

def load_students():
    try:
        with open(FILENAME, "r") as file:
            students = file.read().splitlines()
    except FileNotFoundError:
        students = []
    return students

def save_students(students):
    with open(FILENAME, "w") as file:
        for student in students:
            file.write(student + "\n")

def add_student(students):
    name = input("Enter student name: ")
    marks = input("Enter marks: ")
    student = name + "," + marks
    students.append(student)
    save_students(students)
    print("Student added successfully.")

def show_students(students):
    if len(students) == 0:
        print("No students found.")
    else:
        print("\nStudent List:")
        for student in students:
            name, marks = student.split(",")
            print("Name:", name, "| Marks:", marks)

def search_student(students):
    search = input("Enter student name to search: ")
    found = False
    for student in students:
        name, marks = student.split(",")
        if name == search:
            print("Found → Name:", name, "| Marks:", marks)
            found = True
            break
    if not found:
        print("Student not found.")

def delete_student(students):
    delete = input("Enter student name to delete: ")
    new_list = []
    found = False

    for student in students:
        name, marks = student.split(",")
        if name != delete:
            new_list.append(student)
        else:
            found = True

    if found:
        save_students(new_list)
        print("Student deleted.")
        return new_list
    else:
        print("Student not found.")
        return students

students = load_students()

while True:
    print("\nMenu:")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student(students)

    elif choice == "2":
        show_students(students)

    elif choice == "3":
        search_student(students)

    elif choice == "4":
        students = delete_student(students)

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
