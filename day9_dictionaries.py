students = [
    {"name": "Himanshu", "marks": 85},
    {"name": "Rahul", "marks": 78},
    {"name": "Priya", "marks": 92}
]

name = input("Enter student name: ").strip().title()
marks = int(input("Enter marks: "))

students.append({"name": name, "marks": marks})

print("\nUpdated student list:")

for student in students:
    print(student["name"], "scored", student["marks"])
