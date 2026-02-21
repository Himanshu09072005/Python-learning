import tkinter as tk
from tkinter import messagebox

FILENAME = "students.txt"


def add_student():
    name = name_entry.get()
    marks = marks_entry.get()

    if name == "" or marks == "":
        messagebox.showwarning("Warning", "Please enter name and marks")
        return

    with open(FILENAME, "a") as file:
        file.write(name + "," + marks + "\n")

    messagebox.showinfo("Success", "Student added successfully")

    name_entry.delete(0, tk.END)
    marks_entry.delete(0, tk.END)


def show_students():
    try:
        with open(FILENAME, "r") as file:
            students = file.read()

        if students == "":
            messagebox.showinfo("Students", "No students found")
        else:
            messagebox.showinfo("Students", students)

    except FileNotFoundError:
        messagebox.showinfo("Students", "No students found")


window = tk.Tk()
window.title("Student Management System")
window.geometry("400x300")


name_label = tk.Label(window, text="Enter Name:")
name_label.pack()

name_entry = tk.Entry(window)
name_entry.pack()


marks_label = tk.Label(window, text="Enter Marks:")
marks_label.pack()

marks_entry = tk.Entry(window)
marks_entry.pack()



add_button = tk.Button(window, text="Add Student", command=add_student)
add_button.pack(pady=10)



show_button = tk.Button(window, text="Show Students", command=show_students)
show_button.pack(pady=10)

window.mainloop()