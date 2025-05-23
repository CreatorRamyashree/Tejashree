import tkinter as tk
from tkinter import messagebox

def calculate_interest():
    try:
        principal = float(entry_principal.get())
        rate = float(entry_rate.get())
        time = float(entry_time.get())
        
        si = (principal * rate * time) / 100
        ci = principal * ((1 + rate / 100) ** time) - principal

        label_result_si.config(text=f"Simple Interest: ₹{si:.2f}")
        label_result_ci.config(text=f"Compound Interest: ₹{ci:.2f}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

window = tk.Tk()
window.title("Interest Calculator")
window.geometry("300x300")

tk.Label(window, text="Principal Amount (₹):").pack(pady=5)
entry_principal = tk.Entry(window)
entry_principal.pack()

tk.Label(window, text="Rate of Interest (%):").pack(pady=5)
entry_rate = tk.Entry(window)
entry_rate.pack()

tk.Label(window, text="Time Period (years):").pack(pady=5)
entry_time = tk.Entry(window)
entry_time.pack()

tk.Button(window, text="Calculate", command=calculate_interest).pack(pady=10)

label_result_si = tk.Label(window, text="Simple Interest: ₹0.00")
label_result_si.pack(pady=5)

label_result_ci = tk.Label(window, text="Compound Interest: ₹0.00")
label_result_ci.pack(pady=5)

window.mainloop()
