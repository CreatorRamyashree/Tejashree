import tkinter as tk

def check_strength():
    password = entry_password.get()
    length = len(password)

    if length == 0:
        result_label.config(text="Please enter a password", fg="red")
    elif length < 6:
        result_label.config(text="Weak Password", fg="red")
    elif length < 10:
        result_label.config(text="Moderate Password", fg="orange")
    else:
        result_label.config(text="Strong Password", fg="green")

window = tk.Tk()
window.title("Password Strength Checker")
window.geometry("300x200")

tk.Label(window, text="Enter Password:").pack(pady=10)
entry_password = tk.Entry(window, show="*")
entry_password.pack()

tk.Button(window, text="Check Strength", command=check_strength).pack(pady=10)

result_label = tk.Label(window, text="", font=("Arial", 12))
result_label.pack(pady=10)

window.mainloop()
