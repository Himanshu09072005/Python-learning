import tkinter as tk

def get_response(user_input):
    user_input = user_input.lower()

    if user_input == "hello":
        return "Hi! How can I help you?"
    elif user_input == "how are you":
        return "I am fine. How about you?"
    elif user_input == "your name":
        return "I am your Python chatbot."
    elif user_input == "bye":
        return "Goodbye!"
    else:
        return "I don't understand that yet."

def send_message():
    user_message = entry.get()

    if user_message == "":
        return

    chat_box.insert(tk.END, "You: " + user_message + "\n")

    response = get_response(user_message)

    chat_box.insert(tk.END, "Bot: " + response + "\n\n")

    entry.delete(0, tk.END)

window = tk.Tk()
window.title("Chatbot")
window.geometry("400x500")

chat_box = tk.Text(window, height=20, width=45)
chat_box.pack(pady=10)

entry = tk.Entry(window, width=30)
entry.pack(side=tk.LEFT, padx=10)

send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack(side=tk.LEFT)

window.mainloop()