import tkinter as tk
from tkinter import messagebox

USER_FILE = "users.txt"
MEMORY_FILE = "memory.txt"
CHAT_FILE = "chat_history.txt"

current_user = ""
user_name = ""

def register():
    username = username_entry.get()
    password = password_entry.get()

    if username == "" or password == "":
        messagebox.showerror("Error", "Enter username and password")
        return

    with open(USER_FILE, "a") as file:
        file.write(username + "," + password + "\n")

    messagebox.showinfo("Success", "Registered successfully")

def login():
    global current_user, user_name

    username = username_entry.get()
    password = password_entry.get()

    try:
        with open(USER_FILE, "r") as file:
            users = file.readlines()

        for user in users:
            u, p = user.strip().split(",")
            if u == username and p == password:
                current_user = username
                user_name = load_name()
                login_frame.pack_forget()
                chat_frame.pack()
                return

        messagebox.showerror("Error", "Invalid login")

    except:
        messagebox.showerror("Error", "No users found")

def load_name():
    try:
        with open(MEMORY_FILE, "r") as file:
            return file.read().strip()
    except:
        return ""

def save_name(name):
    with open(MEMORY_FILE, "w") as file:
        file.write(name)

def save_chat(text):
    with open(CHAT_FILE, "a") as file:
        file.write(text + "\n")

def get_response(user_input):
    global user_name

    user_input = user_input.lower()

    if "my name is" in user_input:
        user_name = user_input.replace("my name is", "").strip()
        save_name(user_name)
        return "I will remember you, " + user_name

    elif "hello":
        if user_name != "":
            return "Hello " + user_name
        else:
            return "Hello, tell me your name"

    elif "your name" in user_input:
        return "I am your Smart AI Assistant"

    elif "bye" in user_input:
        return "Goodbye"

    else:
        return "I am learning"

def send_message():
    user_input = entry.get()

    if user_input == "":
        return

    chat_box.insert(tk.END, "You: " + user_input + "\n")
    save_chat("You: " + user_input)

    response = get_response(user_input)

    chat_box.insert(tk.END, "Assistant: " + response + "\n\n")
    save_chat("Assistant: " + response)

    entry.delete(0, tk.END)

window = tk.Tk()
window.title("Smart AI Assistant")
window.geometry("500x600")

login_frame = tk.Frame(window)
login_frame.pack()

tk.Label(login_frame, text="Username").pack()
username_entry = tk.Entry(login_frame)
username_entry.pack()

tk.Label(login_frame, text="Password").pack()
password_entry = tk.Entry(login_frame, show="*")
password_entry.pack()

tk.Button(login_frame, text="Register", command=register).pack(pady=5)
tk.Button(login_frame, text="Login", command=login).pack(pady=5)

chat_frame = tk.Frame(window)

chat_box = tk.Text(chat_frame, height=25, width=55)
chat_box.pack()

entry = tk.Entry(chat_frame, width=35)
entry.pack(side=tk.LEFT)

tk.Button(chat_frame, text="Send", command=send_message).pack(side=tk.LEFT)

window.mainloop()