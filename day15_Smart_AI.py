import tkinter as tk

user_name = ""

def get_response(user_input):
    global user_name
    user_input = user_input.lower()

    if "my name is" in user_input:
        user_name = user_input.replace("my name is", "").strip()
        return "Nice to meet you, " + user_name

    elif "hello" in user_input:
        if user_name != "":
            return "Hello " + user_name + "! How can I help you?"
        else:
            return "Hello! What is your name?"

    elif "your name" in user_input:
        return "I am your Smart AI Assistant."

    elif "how are you" in user_input:
        return "I am working perfectly."

    elif "bye" in user_input:
        return "Goodbye! Have a nice day."

    elif user_input == "":
        return ""

    else:
        return "I am still learning. Please teach me more."

def send_message():
    user_message = entry.get()

    if user_message == "":
        return

    chat_box.insert(tk.END, "You: " + user_message + "\n")
    response = get_response(user_message)
    chat_box.insert(tk.END, "Assistant: " + response + "\n\n")

    entry.delete(0, tk.END)

window = tk.Tk()
window.title("Smart AI Assistant")
window.geometry("500x600")

chat_box = tk.Text(window, height=25, width=55)
chat_box.pack(pady=10)

entry = tk.Entry(window, width=35)
entry.pack(side=tk.LEFT, padx=10)

send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack(side=tk.LEFT)

window.mainloop()