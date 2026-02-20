import tkinter as tk

window = tk.Tk()
window.title("My First GUI App")
window.geometry("400x300")

label = tk.Label(window, text="Welcome Himanshu!", font=("Arial", 16))
label.pack(pady=20)

def on_click():
    label.config(text="Button was clicked!")

button = tk.Button(window, text="Click Me", font=("Arial", 14), command=on_click)
button.pack()

window.mainloop()