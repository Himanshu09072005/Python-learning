import tkinter as tk
from tkinter import messagebox

FILENAME = "users.txt"

def register():
    username = username_entry.get()
    password = password_entry.get()

    if username == "" or password == "":
        messagebox.showwarning("Warning", "Enter username and password")
        return

    with open(FILENAME, "a") as file:
        file.write(username + "," + password + "\n")

    messagebox.showinfo("Success", "Registration successful")

    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

def login():
    username = username_entry.get()
    password = password_entry.get()

    try:
        with open(FILENAME, "r") as file:
            users = file.readlines()

        for user in users:
            u, p = user.strip().split(",")
            if u == username and p == password:
                messagebox.showinfo("Success", "Login successful")
                return

        messagebox.showerror("Error", "Invalid username or password")

    except FileNotFoundError:
        messagebox.showerror("Error", "No users registered")

window = tk.Tk()
window.title("Login System")
window.geometry("400x300")

username_label = tk.Label(window, text="Username")
username_label.pack()

username_entry = tk.Entry(window)
username_entry.pack()

password_label = tk.Label(window, text="Password")
password_label.pack()

password_entry = tk.Entry(window, show="*")
password_entry.pack()

register_button = tk.Button(window, text="Register", command=register)
register_button.pack(pady=10)

login_button = tk.Button(window, text="Login", command=login)
login_button.pack(pady=10)

window.mainloop()